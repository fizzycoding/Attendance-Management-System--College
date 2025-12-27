from PySide6.QtWidgets import QWidget

from controllers.attendance_controller import AttendanceController
from controllers.classes_student_controller import ClassesStudentController
from controllers.classes_teacher_controller import ClassesTeacherController
from controllers.dashboard_student_controller import DashboardStudentController
from controllers.dashboard_teacher_controller import DashboardTeacherController
from controllers.reports_controller import ReportsController
from ui.home_ui import Ui_HomeWindow
from utils.constants import ROLE


class HomeController(QWidget):
    def __init__(self, mainWindow, user):
        super().__init__()
        self.mainWindow = mainWindow
        self.ui = Ui_HomeWindow()
        self.ui.setupUi(self)
        self.user = user
        self.setProfiles()
        self.setupSidebars()
        self.setupPages()
        self.connect_buttons()

    # ------- Set Profile ---------
    def setProfiles(self):
        if self.user:
            print(self.user)
            self.ui.nameLabel.setText(self.user["name"])
            self.ui.usernameLabel.setText(self.user["username"])
        else:
            self.ui.nameLabel.setText("Unknown")
            self.ui.usernameLabel.setText("nousername")

    # ------- Menu setup ---------
    def setupSidebars(self):
        if self.user and self.user["role"] == ROLE.TEACHER:
            self.ui.sidebarStack.setCurrentIndex(1)
        else:
            self.ui.sidebarStack.setCurrentIndex(0)

    # ------- Page setup ---------
    def setupPages(self):
        self.pages = {
            "dashboardT": DashboardTeacherController(self.user),
            "dashboardS": DashboardStudentController(self.user),
            "classesT": ClassesTeacherController(self.user),
            "classesS": ClassesStudentController(self.user),
            "attendance": AttendanceController(self.user),
            "reports": ReportsController(self.user),
        }
        self.pages["classesT"].classModified.connect(self.pages["attendance"].loadClasses)
        self.pages["classesT"].classModified.connect(self.pages["classesS"].refreshCass)

        for page in self.pages.values():
            self.ui.mainContentStack.addWidget(page)

        print(self.user)
        if self.user and self.user["role"] == ROLE.STUDENT:
            self.show("dashboardS")
        else:
            self.show("dashboardT")

    # ---------- button wiring ----------
    def connect_buttons(self):
        self.ui.btn_std_dashboard.clicked.connect(lambda: self.show("dashboardS"))
        self.ui.btn_std_classes.clicked.connect(lambda: self.show("classesS"))
        self.ui.btn_teach_dashboard.clicked.connect(lambda: self.show("dashboardT"))
        self.ui.btn_teach_classes.clicked.connect(lambda: self.show("classesT"))
        self.ui.btn_teach_attendance.clicked.connect(lambda: self.show("attendance"))
        self.ui.btn_teach_reports.clicked.connect(lambda: self.show("reports"))
        self.ui.logoutButton.clicked.connect(lambda: self.mainWindow.showLogin())

    def show(self, key):
        self.ui.mainContentStack.setCurrentWidget(self.pages[key])
