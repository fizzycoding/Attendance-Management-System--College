from PySide6.QtCore import Signal
from PySide6.QtWidgets import QFrame, QMessageBox

from database.database import getDB
from ui.components.test_card import Ui_test_card  # Adjust import path
from utils.constants import ROLE
from utils.message import showQuestionMessage


class TestCardController(QFrame, Ui_test_card):
    deleted = Signal()
    clicked = Signal(int)

    def __init__(self, test_id, name, max_marks, pass_marks, date, role=ROLE.STUDENT, openCallback=None):
        super().__init__()
        self.setupUi(self)
        self.test_id = test_id

        self.test_name.setText(name)
        self.label_max.setText(f"Max: {max_marks}")
        self.label_pass.setText(f"Pass: {pass_marks}")
        self.test_date.setText(date)

        if role == ROLE.STUDENT:
            self.btn_delete.hide()
        else:
            self.btn_delete.show()
            self.btn_delete.clicked.connect(self.deleteTest)

        self.btn_open.clicked.connect(lambda: openCallback(test_id))

    def deleteTest(self):
        reply = showQuestionMessage(
            self, "Delete Test",
            "Are you sure?\nAll marks associated with this test will be lost.",
        )

        if reply == QMessageBox.StandardButton.Yes:
            db = getDB()
            cursor = db.cursor()
            try:
                cursor.execute("DELETE FROM tests WHERE id=?", (self.test_id,))
                db.commit()
                self.deleted.emit()
            except Exception as e:
                print(f"Error deleting test: {e}")
            finally:
                cursor.close()
                db.close()
