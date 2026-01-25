from PySide6.QtWidgets import QDialog

from ui.components.new_class_popup_ui import Ui_CreateClassPopup


class CreateClassPopup(QDialog, Ui_CreateClassPopup):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Create new class")
        self.btn_close.clicked.connect(self.reject)
        self.class_name_input.returnPressed.connect(self.createBTNHandler)
        self.btn_create.clicked.connect(self.createBTNHandler)
        self.setFixedSize(400, 250)

    def createBTNHandler(self):
        val = self.class_name_input.text().strip()
        if val != "" and len(val) <= 100:
            self.accept()
        else:
            self.class_name_input.setStyleSheet("border: 1px solid red;")

    def getClassName(self):
        return self.class_name_input.text()
