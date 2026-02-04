from PySide6.QtCore import QDate
from PySide6.QtWidgets import QWidget, QMessageBox, QSpacerItem, QSizePolicy

from controllers.class_card_controller import ClassCardController
from controllers.join_class_popup_controller import JoinClassPopup
from database.database import getDB
from ui.my_classes_student_ui import Ui_MyClassesStudent
from utils.constants import ROLE
from utils.message import showMessage


class MyClassesStudentController(QWidget):
    def __init__(self, user, openClassfn):
        super().__init__()
        self.ui = Ui_MyClassesStudent()
        self.ui.setupUi(self)
        self.user = user
        self.openClass = openClassfn
        self.ui.btn_join_class.clicked.connect(self.showJoinClassPopup)
        self.loadClasses()
        self.ui.refresh_classes.clicked.connect(self.refresh)

    def refresh(self):
        self.loadClasses()

    def showJoinClassPopup(self):
        popup = JoinClassPopup(parent=self)

        if popup.exec():
            code = popup.getCode()
            self.joinClass(code)

    def joinClass(self, code):
        db = getDB()
        cursor = db.cursor()

        try:
            query = "SELECT * FROM classes WHERE invite_code = ?"
            cursor.execute(query, (code,))
            classData = cursor.fetchone()
            if not classData:
                showMessage(
                    self, "Error", "Invalid Invite Code!", QMessageBox.Icon.Critical
                )
                return
            if classData["created_by"] == self.user["id"]:
                showMessage(
                    self,
                    "Error",
                    "Admin cannot join as a student!",
                    QMessageBox.Icon.Critical,
                )
                return

            query = (
                "SELECT 1 FROM class_members WHERE student_id=? AND class_id=? LIMIT 1"
            )
            cursor.execute(query, (self.user["id"], classData["id"]))
            if cursor.fetchone():
                showMessage(
                    self,
                    "Error",
                    "You are already a member of this class.",
                    QMessageBox.Icon.Critical,
                )
                return

            query = "INSERT INTO class_members(class_id, student_id) VALUES(?, ?)"
            cursor.execute(query, (classData["id"], self.user["id"]))
            db.commit()
            showMessage(
                self,
                "Success",
                f"Successfully joined {classData['class_name']}!",
                QMessageBox.Icon.Information,
            )
            self.loadClasses()
        except Exception as e:
            db.rollback()
            print(e)
        finally:
            cursor.close()
            db.close()

    def loadClasses(self):
        while self.ui.classesLayout.count():
            item = self.ui.classesLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        db = getDB()
        cursor = db.cursor()
        today_str = QDate.currentDate().toString("yyyy-MM-dd")
        try:
            query = """
                SELECT 
                    c.id,
                    c.class_name,

                    (SELECT COUNT(*) FROM class_members WHERE class_id = c.id) as total_students,

                    (SELECT COUNT(*)
                            FROM attendance_records r
                            JOIN attendance_sessions s ON r.session_id = s.id
                            WHERE s.class_id = c.id AND s.date = ? AND r.status = 'present'
                    ) as total_present,

                    (SELECT COUNT(*) 
                         FROM attendance_records ar 
                         JOIN attendance_sessions s ON ar.session_id = s.id 
                         WHERE s.class_id = c.id AND s.date = ? AND ar.status = 'absent'
                    ) as total_absent

                FROM classes c
                JOIN class_members cm ON c.id = cm.class_id 
                WHERE cm.student_id=?"""
            cursor.execute(query, (today_str, today_str, self.user["id"]))

            rows = cursor.fetchall()
            if not rows:
                self.ui.classes_stacked.setCurrentWidget(self.ui.no_class)
            else:
                self.ui.classes_stacked.setCurrentWidget(self.ui.all_class)

                for row in rows:
                    card = ClassCardController(
                        classId=str(row["id"]),
                        className=row["class_name"],
                        present=row["total_present"],
                        absent=row["total_absent"],
                        total=row["total_students"],
                        role=ROLE.STUDENT
                    )
                    card.clicked.connect(self.openClass)
                    self.ui.classesLayout.addWidget(card)

            spacer = QSpacerItem(
                20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
            )
            self.ui.classesLayout.addItem(spacer)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            db.close()
