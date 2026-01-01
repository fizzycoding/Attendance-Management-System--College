from PySide6.QtWidgets import QWidget, QSpacerItem, QSizePolicy

from controllers.student_marks_row_controller import StudentMarksRowController
from database.database import getDB
from ui.test_details_page import Ui_test_details_page  # Adjust import
from utils.message import showMessage


class TestDetailsController(QWidget):
    def __init__(self, user, test_id, back_callback=None):
        super().__init__()
        self.ui = Ui_test_details_page()
        self.ui.setupUi(self)
        self.user = user
        self.test_id = test_id

        self.max_marks = 0
        self.passing_marks = 0

        if back_callback:
            self.ui.btn_back.clicked.connect(back_callback)
        else:
            self.ui.btn_back.hide()

        self.ui.btn_save_marks.clicked.connect(self.saveMarks)

        self.loadTestDetails()
        self.loadStudents()

    def loadTestDetails(self):
        db = getDB()
        cursor = db.cursor()
        try:
            query = "SELECT test_name, max_marks, passing_marks, test_date FROM tests WHERE id=?"
            cursor.execute(query, (self.test_id,))

            row = cursor.fetchone()
            if row:
                if isinstance(row, tuple):
                    data = {"test_name": row[0], "max_marks": row[1], "passing_marks": row[2], "test_date": row[3]}
                else:
                    data = row

                self.ui.label_test_name.setText(data["test_name"])
                self.max_marks = data["max_marks"]
                self.passing_marks = data["passing_marks"]  # Save this!

                self.ui.label_max.setText(f"Max Marks: {self.max_marks}")
                self.ui.label_pass.setText(f"Passing: {self.passing_marks}")
                self.ui.label_date.setText(f"Date: {data['test_date']}")

        except Exception as e:
            print(f"Error loading test details: {e}")
        finally:
            cursor.close()
            db.close()

    def loadStudents(self):
        while self.ui.studentsLayout.count():
            item = self.ui.studentsLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        db = getDB()
        cursor = db.cursor()
        try:
            query = """
                SELECT 
                    c.id as member_id, 
                    u.name, 
                    tr.marks_obtained
                FROM class_members c
                JOIN users u ON c.student_id = u.id
                LEFT JOIN test_results tr ON tr.member_id = c.id AND tr.test_id = ?
                WHERE c.class_id = (SELECT class_id FROM tests WHERE id = ?)
                ORDER BY u.name ASC
            """
            cursor.execute(query, (self.test_id, self.test_id))
            rows = cursor.fetchall()

            for i, row in enumerate(rows):
                if isinstance(row, tuple):
                    member_id = row[0]
                    name = row[1]
                    marks = row[2]
                else:
                    member_id = row['member_id']
                    name = row['name']
                    marks = row['marks_obtained']

                row_widget = StudentMarksRowController(
                    sNo=i + 1,
                    name=name,
                    member_id=member_id,
                    marks=marks,
                    max_marks=self.max_marks,
                    passing_marks=self.passing_marks
                )
                self.ui.studentsLayout.addWidget(row_widget)

            self.ui.studentsLayout.addItem(
                QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        except Exception as e:
            print(f"Error loading students: {e}")
        finally:
            cursor.close()
            db.close()

    def saveMarks(self):
        db = getDB()
        cursor = db.cursor()
        try:
            layout = self.ui.studentsLayout
            for i in range(layout.count()):
                item = layout.itemAt(i)
                widget = item.widget()
                if isinstance(widget, StudentMarksRowController):
                    member_id = widget.member_id
                    if widget.isAttempted():
                        marks = widget.getMarks()

                        query = """
                            INSERT INTO test_results (test_id, member_id, marks_obtained)
                            VALUES (?, ?, ?)
                            ON CONFLICT(test_id, member_id) 
                            DO UPDATE SET marks_obtained=excluded.marks_obtained
                        """
                        cursor.execute(query, (self.test_id, member_id, marks))
                    else:
                        query = "DELETE FROM test_results WHERE test_id = ? AND member_id = ?"
                        cursor.execute(query, (self.test_id, member_id))

            db.commit()
            showMessage(self, "Success", "Marks saved successfully!")
            self.loadStudents()

        except Exception as e:
            db.rollback()
            print(f"Error saving marks: {e}")
            showMessage(self, "Error", "Failed to save marks.")
        finally:
            cursor.close()
            db.close()
