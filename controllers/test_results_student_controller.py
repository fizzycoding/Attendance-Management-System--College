from PySide6.QtWidgets import QWidget, QSpacerItem, QSizePolicy

from controllers.test_result_student_row_controller import StudentTestRowController
from database.database import getDB
from ui.test_results_student_ui import Ui_student_test_results


class StudentTestResultController(QWidget):
    def __init__(self, user):
        super().__init__()
        self.ui = Ui_student_test_results()
        self.ui.setupUi(self)
        self.user = user
        self.load_classes()
        self.ui.classes_drpdown.currentIndexChanged.connect(self.load_tests)

    def refresh(self):

        current_class_id = self.ui.classes_drpdown.currentData()

        self.load_classes()
        if current_class_id:
            index = self.ui.classes_drpdown.findData(current_class_id)
            if index >= 0:
                self.ui.classes_drpdown.setCurrentIndex(index)

    def load_classes(self):
        self.ui.classes_drpdown.blockSignals(True)
        self.ui.classes_drpdown.clear()

        db = getDB()
        cursor = db.cursor()

        try:
            cursor.execute("""
                SELECT c.id, c.class_name 
                FROM class_members cm
                JOIN classes c ON cm.class_id = c.id
                WHERE cm.student_id = ?
            """, (self.user['id'],))
            classes = cursor.fetchall()

            if classes:
                for cls in classes:
                    self.ui.classes_drpdown.addItem(cls[1], cls[0])
                self.ui.classes_drpdown.blockSignals(False)
                self.load_tests()
                if self.ui.classes_drpdown.count() > 0:
                    self.ui.classes_drpdown.setCurrentIndex(0)
            else:
                self.ui.classes_drpdown.addItem("No Classes Joined")
                self.ui.main_stack.setCurrentWidget(self.ui.page_no_tests)
                self.ui.label_empty.setText("Join a class to see results.")

        except Exception as e:
            print(f"Error loading classes: {e}")
        finally:
            cursor.close()
            db.close()

    def load_tests(self):
        """Fetch tests for the selected class."""
        class_id = self.ui.classes_drpdown.currentData()
        if not class_id:
            return

        # Clear existing rows from the scroll area
        self._clear_layout(self.ui.container_tests)

        db = getDB()
        cursor = db.cursor()

        try:
            # Query: Test Info + Student Result (LEFT JOIN)
            # We need to find the student's 'member_id' for this specific class first
            cursor.execute("""
                SELECT 
                    t.test_name, 
                    t.test_date, 
                    t.max_marks, 
                    t.passing_marks,
                    tr.marks_obtained
                FROM tests t
                LEFT JOIN test_results tr ON tr.test_id = t.id AND tr.member_id = (
                    SELECT id FROM class_members WHERE class_id = ? AND student_id = ?
                )
                WHERE t.class_id = ?
                ORDER BY t.test_date DESC
            """, (class_id, self.user['id'], class_id))

            tests = cursor.fetchall()

            if not tests:
                self.ui.main_stack.setCurrentWidget(self.ui.page_no_tests)
                self.ui.label_empty.setText("No tests found for this class.")
            else:
                self.ui.main_stack.setCurrentWidget(self.ui.page_test_list)

                for t in tests:
                    # Create Row Controller
                    row = StudentTestRowController(t)
                    self.ui.container_tests.addWidget(row)

                # Add Spacer at bottom so rows stick to the top
                spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
                self.ui.container_tests.addItem(spacer)

        except Exception as e:
            print(f"Error loading tests: {e}")
        finally:
            cursor.close()
            db.close()

    def _clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
            elif item.spacerItem():
                layout.removeItem(item)
