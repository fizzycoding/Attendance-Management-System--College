import random
import string

import mysql.connector
from PySide6.QtWidgets import QWidget, QSpacerItem, QSizePolicy

from controllers.class_card_controller import ClassCardController
from controllers.create_class_popup_controller import CreateClassPopup
from database.database import getDB
from ui.classes_teacher_ui import Ui_classes_teacher


class ClassesTeacherController(QWidget):
    def __init__(self, user):
        super().__init__()
        self.ui = Ui_classes_teacher()
        self.ui.setupUi(self)
        self.user = user
        self.ui.btn_new_class.clicked.connect(self.showCreateClassPopup)
        self.loadClasses()

    def showCreateClassPopup(self):
        popUp = CreateClassPopup(parent=self)

        if popUp.exec():
            name = popUp.getClassName()
            self.createNewClass(name)

    def createNewClass(self, name):
        db = getDB()
        cursor = db.cursor()
        user_id = self.user["id"]
        new_class_id = None

        while True:
            code = self.generateInviteCode()
            try:
                query = "INSERT INTO classes(class_name, invite_code, created_by) VALUES (%s, %s, %s)"
                print(code)
                cursor.execute(query, (name, code, user_id))
                db.commit()
                new_class_id = cursor.lastrowid
                break
            except mysql.connector.IntegrityError as e:
                if e.errno == 1062:
                    continue
            except Exception as e:
                db.rollback()
                print(e)

        db.close()
        cursor.close()

        if new_class_id:
            self.insertClassToUi(new_class_id, name, 0, 0, 0)

    def generateInviteCode(self, length=6):
        chars = string.ascii_uppercase + string.digits
        code = "".join(random.choices(chars, k=length))
        return code

    def loadClasses(self):
        # ---- DELETE the prev elements -----
        while self.ui.classesLayout.count():
            item = self.ui.classesLayout.takeAt(0)
            if (item.widget()):
                item.widget().deleteLater()

        # --- Main code ---
        db = getDB()
        cursor = db.cursor(dictionary=True)
        try:
            query = "SELECT id, class_name, invite_code FROM classes WHERE created_by=%s"
            cursor.execute(query, (self.user["id"],))
            rows = cursor.fetchall()

            if len(rows) <= 0:
                self.ui.classes_stacked.setCurrentWidget(self.ui.no_class)
            else:
                self.ui.classes_stacked.setCurrentWidget(self.ui.all_class)

            for row in rows[0:3]:
                classId = row["id"]
                name = row["class_name"]
                self.insertClassToUi(classId, name)

            # ---- spacer -----
            spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
            self.ui.classesLayout.addItem(spacer)
        except Exception as e:
            db.rollback()
            print(e)

        db.close()
        cursor.close()

    def insertClassToUi(self, id, name, total=0, present=0, absent=0):
        card = ClassCardController(str(id), name, total, present, absent)
        card.clicked.connect(self.openClass)
        self.ui.classesLayout.insertWidget(0, card)

    def openClass(self, id):
        print(id)
