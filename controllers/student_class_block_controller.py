from PySide6.QtCore import Signal
from PySide6.QtWidgets import QFrame, QMessageBox

from controllers.edit_name_popup_controller import EditNamePopup
from database.database import getDB
from ui.components.student_class_block import Ui_student_block
from utils.constants import ATTENDANCE_STATUS
from utils.constants import ROLE
from utils.message import showMessage, showQuestionMessage


class StudentClassBlockController(QFrame, Ui_student_block):
    studentModified = Signal()

    def __init__(self, id, sNo, name, attendanceRate=0, status=None, role=ROLE.STUDENT, isCurrent=False, classId=None):
        super().__init__()
        self.setupUi(self)
        self.id = id
        self.classId = classId
        self.studentName = name
        self.serial_number.setText(str(sNo))
        self.name.setText(name)
        self.updateStatusStyle(status)
        if role == ROLE.STUDENT:
            self.btn_remove_student.hide()
            self.btn_edit.hide()
        else:
            self.btn_remove_student.show()
            self.btn_edit.show()
            self.btn_remove_student.clicked.connect(self.removeStudent)
            self.btn_edit.clicked.connect(self.editStudentName)
        if isCurrent:
            self.setObjectName("me")
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

    def editStudentName(self):
        popup = EditNamePopup(
            title="Edit Student Name",
            field_label="Student name",
            placeholder="Enter student name",
            default_value=self.studentName,
            min_length=2,
            max_length=50,
            parent=self
        )

        if popup.exec():
            new_name = popup.get_value().strip()

            if new_name == self.studentName:
                showMessage(self, "Info", "Student name is unchanged.")
                return

            db = getDB()
            cursor = db.cursor()

            try:
                update_query = """
                    UPDATE class_members
                    SET guest_name = ?
                    WHERE id = ? AND class_id = ?
                """
                cursor.execute(update_query, (new_name, self.id, self.classId))
                db.commit()

                if cursor.rowcount == 0:
                    showMessage(self, "Error", "Update failed. Student not found or no permission.")
                    return

                self.studentName = new_name
                self.name.setText(new_name)

                showMessage(self, "Success", "Student name updated successfully.")

            except Exception as e:
                print("Failed to update student name:", e)
                showMessage(self, "Error", "Failed to update student name.")
            finally:
                cursor.close()
                db.close()

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
