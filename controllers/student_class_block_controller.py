from PySide6.QtCore import Signal
from PySide6.QtWidgets import QFrame, QMessageBox

from database.database import getDB
from ui.components.student_class_block import Ui_student_block
from utils.constants import ATTENDANCE_STATUS
from utils.constants import ROLE
from utils.message import showMessage, showQuestionMessage


class StudentClassBlockController(QFrame, Ui_student_block):
    studentModified = Signal()

    def __init__(self, id, sNo, name, member_id, attendanceRate=0, status=None, role=ROLE.STUDENT):
        super().__init__()
        self.setupUi(self)
        self.id = id
        self.studentName = name
        self.member_id = member_id
        self.serial_number.setText(str(sNo))
        self.name.setText(name)
        self.updateStatusStyle(status)
        if role == ROLE.STUDENT:
            self.btn_remove_student.hide()
        else:
            self.btn_remove_student.show()
            self.btn_remove_student.clicked.connect(self.removeStudent)

        if attendanceRate:
            self.attendance_rate_label.setText(f"{round(attendanceRate)}%")
            self.progressBar_attendance_rate.setValue(round(attendanceRate))
        else:
            self.attendance_rate_label.setText("00%")
            self.progressBar_attendance_rate.setValue(0)

    def updateStatusStyle(self, status):
        if status == ATTENDANCE_STATUS.PRESENT:
            new_name = "status_present"
            text = "Present"
        elif status == ATTENDANCE_STATUS.ABSENT:
            new_name = "status_absent"
            text = "Absent"
        else:
            new_name = "status_not_marked"
            text = "Not Marked"

        self.btn_status.setObjectName(new_name)
        self.btn_status.setText(text)
        self.btn_status.style().unpolish(self.btn_status)
        self.btn_status.style().polish(self.btn_status)

    def removeStudent(self):
        reply = showQuestionMessage(self, "Remove student",
                                    f"Are you sure you want to remove {self.studentName} from the class?")
        if reply == QMessageBox.StandardButton.No:
            return
        db = getDB()
        cursor = db.cursor()
        try:
            query = "DELETE FROM class_members WHERE id = ?"
            cursor.execute(query, (self.id,))
            db.commit()
            self.studentModified.emit()
            showMessage(self, "Success", f"{self.studentName} removed from the class")
            self.deleteLater()
        except Exception as e:
            db.rollback()
            showMessage(self, "Failed", "Failed to remove user", QMessageBox.Icon.Critical)
            print(f"Failed to remove user: {e}")
        finally:
            cursor.close()
            db.close()
