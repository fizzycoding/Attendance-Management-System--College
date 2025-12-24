from PySide6.QtWidgets import QDialog

from ui.components.join_class_popup_ui import Ui_JoinClassPopup


class JoinClassPopup(QDialog, Ui_JoinClassPopup):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Join class")
        self.btn_close.clicked.connect(self.reject)
        self.btn_create.clicked.connect(self.joinBTNHandler)
        self.setFixedSize(400, 250)

    def joinBTNHandler(self):
        val = self.class_name_input.text().strip()

        if val != "" and len(val) <= 6:
            self.accept()
        else:
            self.class_name_input.setStyleSheet("border: 1px solid red;")

    def getCode(self):
        return self.class_name_input.text()
