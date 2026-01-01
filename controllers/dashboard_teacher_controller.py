from PySide6.QtWidgets import QWidget

from ui.dashboard_teacher_ui import Ui_dashboard_page


class DashboardTeacherController(QWidget):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.ui = Ui_dashboard_page()
        self.ui.setupUi(self)
