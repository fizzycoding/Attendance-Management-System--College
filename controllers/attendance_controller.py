from PySide6.QtWidgets import QWidget

from database.database import getDB
from ui.attendance_ui import Ui_attendance_page


class AttendanceController(QWidget):
    def __init__(self, user):
        super().__init__()
        self.ui = Ui_attendance_page()
        self.ui.setupUi(self)
        self.user = user
        self.loadClasses()
        self.ui.dropdown_classes.currentIndexChanged.connect(self.updateInviteCodeUI)
        self.updateInviteCodeUI()

    def loadClasses(self):
        self.ui.dropdown_classes.clear()
        db = getDB()
        cursor = db.cursor(dictionary=True)
        try:
            query = "SELECT id, class_name, invite_code FROM classes WHERE created_by=%s"
            cursor.execute(query, (self.user['id'],))

            rows = cursor.fetchall()

            for row in rows:
                classData = {
                    "id": row["id"],
                    "code": row["invite_code"]
                }
                self.ui.dropdown_classes.addItem(row["class_name"], classData)

        except Exception as e:

            print("Error loading classes:", e)
        finally:
            cursor.close()
            db.close()

    def updateInviteCodeUI(self):
        data = self.ui.dropdown_classes.currentData()
        if data:
            code = data["code"]
            self.ui.invteCode_box.setText(code)
        else:
            self.ui.invteCode_box.setText("------")
