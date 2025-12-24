from PySide6.QtWidgets import QWidget, QMessageBox, QSpacerItem, QSizePolicy

from controllers.class_card_controller import ClassCardController
from controllers.join_class_popup_controller import JoinClassPopup
from database.database import getDB
from ui.classes_student_ui import Ui_classes_student
from utils.constants import ROLE
from utils.message import showMessage


class ClassesStudentController(QWidget):
    def __init__(self, user):
        super().__init__()
        self.ui = Ui_classes_student()
        self.ui.setupUi(self)
        self.user = user
        self.ui.btn_join_class.clicked.connect(self.showJoinClassPopup)
        self.loadClasses()

    def showJoinClassPopup(self):
        popup = JoinClassPopup()

        if popup.exec():
            code = popup.getCode()
            self.joinClass(code)

    def joinClass(self, code):
        db = getDB()
        cursor = db.cursor(dictionary=True)

        try:
            query = "SELECT * FROM classes WHERE invite_code = %s"
            cursor.execute(query, (code,))
            classData = cursor.fetchone()
            if not classData:
                showMessage(self, "Error", "Invalid Invite Code!", QMessageBox.Icon.Critical)
                return
            if classData["created_by"] == self.user["id"]:
                showMessage(self, "Error", "Admin cannot join as a student!", QMessageBox.Icon.Critical)
                return

            query = "SELECT 1 FROM class_members WHERE student_id=%s AND class_id=%s LIMIT 1"
            cursor.execute(query, (self.user["id"], classData["id"]))
            if cursor.fetchone():
                showMessage(self, "Error", "You are already a member of this class.", QMessageBox.Icon.Critical)
                return

            query = "INSERT INTO class_members(class_id, student_id) VALUES(%s, %s)"
            cursor.execute(query, (classData["id"], self.user["id"]))
            db.commit()
            showMessage(self, "Success", f"Successfully joined {classData['class_name']}!",
                        QMessageBox.Icon.Information)
            self.loadClasses()
        except Exception as e:
            db.rollback()
            print(e)

        db.close()
        cursor.close()

    def loadClasses(self):

        while self.ui.classesLayout.count():
            item = self.ui.classesLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        db = getDB()
        cursor = db.cursor(dictionary=True)

        try:
            query = "SELECT classes.id, classes.class_name FROM classes JOIN class_members ON classes.id = class_members.class_id WHERE class_members.student_id=%s"
            cursor.execute(query, (self.user["id"],))

            rows = cursor.fetchall()
            if not rows:
                self.ui.classes_stacked.setCurrentWidget(self.ui.no_class)
            else:
                self.ui.classes_stacked.setCurrentWidget(self.ui.all_class)

                for row in rows:
                    card = ClassCardController(str(row['id']), row['class_name'], 0, 0, 0, ROLE.STUDENT)
                    self.ui.classesLayout.addWidget(card)

            spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
            self.ui.classesLayout.addItem(spacer)
        except Exception as e:
            print(e)

        db.close()
        cursor.close()
