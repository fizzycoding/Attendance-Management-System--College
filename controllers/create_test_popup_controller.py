from PySide6.QtCore import QDate
from PySide6.QtWidgets import QDialog, QMessageBox

from ui.components.create_test_popup import Ui_CreateTestPopup
from utils.message import showMessage


class CreateTestPopup(QDialog, Ui_CreateTestPopup):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.input_date.setDate(QDate.currentDate())

        self.btn_cancel.clicked.connect(self.reject)
        self.btn_create.clicked.connect(self.validateAndAccept)

        self.input_test_name.returnPressed.connect(self.validateAndAccept)
        self.input_pass_marks.returnPressed.connect(self.validateAndAccept)
        self.input_max_marks.returnPressed.connect(self.validateAndAccept)
        self.input_date.returnPressed.connect(self.validateAndAccept)

    def validateAndAccept(self):
        name = self.input_test_name.text().strip()
        max_marks = self.input_max_marks.value()
        pass_marks = self.input_pass_marks.value()

        if not name:
            showMessage(self, "Error", "Test Name cannot be empty!", QMessageBox.Icon.Critical)
            self.input_test_name.setFocus()
            return

        if pass_marks > max_marks:
            showMessage(self, "Error", "Passing marks cannot be greater than Maximum marks!", QMessageBox.Icon.Critical)
            self.input_pass_marks.setFocus()
            return

        self.accept()

    def getTestName(self):
        return self.input_test_name.text().strip()

    def getMaxMarks(self):
        return self.input_max_marks.value()

    def getPassingMarks(self):
        return self.input_pass_marks.value()

    def getDate(self):
        # Returns string in standard DB format (YYYY-MM-DD)
        return self.input_date.date().toString("yyyy-MM-dd")
