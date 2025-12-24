from PySide6.QtWidgets import QWidget

from ui.dashboard_teacher_ui import Ui_Form


class DashboardTeacherController(QWidget):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.ui = Ui_Form()
        self.ui.setupUi(self)
