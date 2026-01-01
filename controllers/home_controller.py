from PySide6.QtWidgets import QWidget

from controllers.attendance_controller import AttendanceController
from controllers.class_open_controller import ClassOpenController
from controllers.classes_student_controller import ClassesStudentController
from controllers.classes_teacher_controller import ClassesTeacherController
from controllers.dashboard_student_controller import DashboardStudentController
from controllers.dashboard_teacher_controller import DashboardTeacherController
from controllers.reports_controller import ReportsController
from controllers.test_details_controller import TestDetailsController
from controllers.test_result_controller import TestResultController
from ui.home_ui import Ui_HomeWindow
from utils.constants import ROLE


class HomeController(QWidget):
    def __init__(self, mainWindow, user):
        super().__init__()
        self.mainWindow = mainWindow
        self.ui = Ui_HomeWindow()
        self.ui.setupUi(self)
        self.user = user
        self.currentClassWidget = None
        self.currentTestDetailed = None

        self.setProfiles()
        self.setupSidebars()
        self.setupPages()
        self.connect_buttons()

    # ------- Set Profile ---------
    def setProfiles(self):
        if self.user:
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
            "classesT": ClassesTeacherController(self.user, self),
            "classesS": ClassesStudentController(self.user),
            "attendance": AttendanceController(self.user),
            "testResults": TestResultController(self.user, self.testDetailsOpen),
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
        self.ui.btn_teach_dashboard.clicked.connect(self.showDashboardTeacher)
        self.ui.btn_teach_classes.clicked.connect(self.showClassesTeacher)
        self.ui.btn_teach_attendance.clicked.connect(self.showAttendance)
        self.ui.btn_results.clicked.connect(self.showTestResults)
        self.ui.btn_teach_reports.clicked.connect(self.showReports)
        self.ui.logoutButton.clicked.connect(lambda: self.mainWindow.showLogin())

    def classOpen(self, classId):
        self.currentClassWidget = ClassOpenController(self.user, self, classId)
        self.ui.mainContentStack.addWidget(self.currentClassWidget)
        self.ui.mainContentStack.setCurrentWidget(self.currentClassWidget)

    def closeClassOpened(self):
        # Remove and cleanup
        if self.currentClassWidget:
            self.ui.mainContentStack.removeWidget(self.currentClassWidget)
            self.currentClassWidget.deleteLater()
            self.currentClassWidget = None

        if self.user["role"] == ROLE.TEACHER:
            self.show("classesT")
        else:
            self.show("classesS")

    def testDetailsOpen(self, testId):
        self.currentTestDetailed = TestDetailsController(self.user, testId, self.closeTestDetails)
        self.ui.mainContentStack.addWidget(self.currentTestDetailed)
        self.ui.mainContentStack.setCurrentWidget(self.currentTestDetailed)

    def closeTestDetails(self):
        if self.currentTestDetailed:
            self.ui.mainContentStack.removeWidget(self.currentTestDetailed)
            self.currentTestDetailed.deleteLater()
            self.currentTestDetailed = None

        self.showTestResults()

    def show(self, key):
        self.ui.mainContentStack.setCurrentWidget(self.pages[key])

    def showClassesTeacher(self):
        self.show("classesT")
        self.pages["classesT"].refresh()

    def showAttendance(self):
        self.show("attendance")
        self.pages["attendance"].refresh()

    def showTestResults(self):
        self.show("testResults")
        self.pages["testResults"].refresh()

    def showReports(self):
        self.show("reports")
        self.pages["reports"].refresh()

    def showDashboardTeacher(self):
        self.show("dashboardT")
        self.pages["dashboardT"].refresh()
