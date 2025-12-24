from PySide6.QtWidgets import QWidget

from ui.view_reports_ui import Ui_Form


class ReportsController(QWidget):
    def __init__(self, user):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.user = user
