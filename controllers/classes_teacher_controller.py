import random
import sqlite3
import string

from PySide6.QtCore import Signal, QDate
from PySide6.QtWidgets import QWidget, QSpacerItem, QSizePolicy

from controllers.class_card_controller import ClassCardController
from controllers.create_class_popup_controller import CreateClassPopup
from database.database import getDB
from ui.classes_teacher_ui import Ui_classes_teacher


class ClassesTeacherController(QWidget):
    classModified = Signal()

    def __init__(self, user, home):
        super().__init__()
        self.ui = Ui_classes_teacher()
        self.ui.setupUi(self)
        self.home = home
        self.user = user
        self.ui.btn_new_class.clicked.connect(self.showCreateClassPopup)
        self.loadClasses()
        self.ui.refresh_class.clicked.connect(self.refresh)

    def refresh(self):
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
                query = "INSERT INTO classes(class_name, invite_code, created_by) VALUES (?, ?, ?)"
                cursor.execute(query, (name, code, user_id))
                db.commit()
                new_class_id = cursor.lastrowid
                break
            except sqlite3.IntegrityError as e:
                if "UNIQUE constraint failed: classes.invite_code" in str(e):
                    continue
                else:
                    print("Integrity error:", e)
                    break

            except Exception as e:
                db.rollback()
                print(e)

        cursor.close()
        db.close()

        if new_class_id:
            self.insertClassToUi(new_class_id, name, 0, 0, 0)
            self.classModified.emit()
        self.loadClasses()

    def generateInviteCode(self, length=6):
        chars = string.digits
        code = "".join(random.choices(chars, k=length))
        return code

    def loadClasses(self):
        # ---- DELETE the prev elements -----
        while self.ui.classesLayout.count():
            item = self.ui.classesLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        # --- Main code ---
        date_str = QDate.currentDate().toString("yyyy-MM-dd")
        db = getDB()
        cursor = db.cursor()
        try:
            query = """
                SELECT 
                    c.id,
                    c.class_name,
                    c.invite_code ,
                    
                    (SELECT COUNT(*) FROM class_members WHERE class_id = c.id) as total_students,
                    
                    (SELECT COUNT(*)
                        FROM attendance_records r
                        JOIN attendance_sessions s ON r.session_id = s.id
                        WHERE s.class_id = c.id AND s.date = ? AND r.status = 'present'
                    ) as total_present,
                    
                    (SELECT COUNT(*) 
                     FROM attendance_records r 
                     JOIN attendance_sessions s ON r.session_id = s.id 
                     WHERE s.class_id = c.id AND s.date = ? AND r.status = 'absent'
                    ) as total_absent
                    
                FROM classes c
                WHERE created_by=?
            """
            cursor.execute(query, (date_str, date_str, self.user["id"]))
            rows = cursor.fetchall()

            print(rows)
            if len(rows) <= 0:
                self.ui.classes_stacked.setCurrentWidget(self.ui.no_class)
            else:
                self.ui.classes_stacked.setCurrentWidget(self.ui.all_class)

            for row in rows:
                classId = row["id"]
                name = row["class_name"]
                total = row["total_students"]
                present = row["total_present"]
                absent = row["total_absent"]
                self.insertClassToUi(classId, name, total, present, absent)

            # ---- spacer -----
            spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
            self.ui.classesLayout.addItem(spacer)
        except Exception as e:
            db.rollback()
            print(e)
        finally:
            cursor.close()
            db.close()

    def insertClassToUi(self, id, name, total=0, present=0, absent=0):
        card = ClassCardController(str(id), name, total, present, absent, user=self.user)
        card.clicked.connect(self.openClass)
        card.deleted.connect(self.deleteClass)
        self.ui.classesLayout.insertWidget(0, card)

    def openClass(self, id):
        self.home.classOpen(id)

    def deleteClass(self):
        self.loadClasses()
        self.classModified.emit()
