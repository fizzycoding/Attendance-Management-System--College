from PySide6.QtCore import Signal
from PySide6.QtWidgets import QFrame, QMessageBox

from controllers.edit_name_popup_controller import EditNamePopup
from database.database import getDB
from ui.components.class_card_ui import Ui_class_card
from utils.constants import ROLE
from utils.message import showMessage, showQuestionMessage


class ClassCardController(QFrame, Ui_class_card):
    clicked = Signal(str)
    deleted = Signal()

    def __init__(self, classId, className, total, present, absent, role=ROLE.TEACHER, user=None):
        super().__init__()
        self.setupUi(self)
        self.user = user
        self.classId = classId
        self.className = className
        self.class_name.setText(className)
        self.total_user_label.setText(str(total))
        self.present_label.setText(str(present))
        self.absent_label.setText(str(absent))
        if role == ROLE.STUDENT:
            self.btn_delete.hide()
            self.btn_edit.hide()
        else:
            self.btn_delete.show()
            self.btn_edit.show()
            self.btn_edit.clicked.connect(self.editClass)
            self.btn_delete.clicked.connect(self.deleteClass)

    def editClass(self):
        popup = EditNamePopup(
            title="Edit Class",
            field_label="Class name",
            placeholder="Enter class name",
            default_value=self.className,
            min_length=2,
            max_length=30,
            parent=self
        )

        if popup.exec():
            new_name = popup.get_value().strip()
            print(new_name)
            if new_name == self.className:
                showMessage(self, "Info", "Class name is unchanged.")
                return

            db = getDB()
            cursor = db.cursor()

            try:
                update_query = "UPDATE classes SET class_name = ? WHERE id = ? AND created_by = ?"
                cursor.execute(update_query, (new_name, self.classId, self.user["id"]))
                db.commit()

                if cursor.rowcount == 0:
                    showMessage(self, "Error", "Update failed. Class not found or no permission.")
                    return

                self.className = new_name
                self.class_name.setText(new_name)

                showMessage(self, "Success", "Class name updated successfully.")

            except Exception as e:
                print("Failed to update class name:", e)
                showMessage(self, "Error", "Failed to update class name.")
            finally:
                cursor.close()
                db.close()

    def deleteClass(self):
        reply = showQuestionMessage(
            self,
            "Delete Class",
            f"Are you sure you want to delete this class?\n{self.className}\nThis action cannot be Undone",
        )

        if reply == QMessageBox.StandardButton.Yes:
            db = getDB()
            cursor = db.cursor()
            try:
                query = "DELETE FROM classes WHERE id=? AND created_by = ?"
                cursor.execute(query, (self.classId, self.user["id"]))
                db.commit()
                showMessage(self, "Success", f"Class {self.className} deleted successfully.")
                self.deleteLater()
                self.deleted.emit()  # Notify parent if needed
            except Exception as e:
                print(f"Failed to delete class {e}")
                showMessage(self, "Error", "Failed")
            finally:
                cursor.close()
                db.close()

    def mousePressEvent(self, event):
        self.clicked.emit(self.classId)
        super().mousePressEvent(event)
