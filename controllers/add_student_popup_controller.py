from PySide6.QtWidgets import QDialog

from ui.components.add_student_popup import Ui_AddStudentPopup


class AddStudentPopupController(QDialog, Ui_AddStudentPopup):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btn_add.clicked.connect(self.onAddClick)
        self.setWindowTitle("Add new student")
        self.student_name_input.returnPressed.connect(self.onAddClick)

    def onAddClick(self):
        name = self.student_name_input.text()
        if name.strip() == "":
            return
        if len(name.strip()) > 100:
            return

        self.accept()

    def getName(self):
        return self.student_name_input.text().strip()
