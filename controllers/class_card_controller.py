from PySide6.QtCore import Signal
from PySide6.QtWidgets import QFrame, QMessageBox

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
        else:
            self.btn_delete.show()
            self.btn_delete.clicked.connect(self.deleteClass)

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
