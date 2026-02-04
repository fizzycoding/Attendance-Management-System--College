import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from controllers.home_controller import HomeController
from controllers.login_controller import LoginController
from controllers.signup_controller import SignupController
from database.seed import init_db


class MainWindow(QMainWindow):
    def __init__(self):
        # Some setup
        super().__init__()
        self.home = None
        self.setMinimumSize(850, 580)
        self.setWindowTitle("Academic Tracker")
        self.icon = QIcon("icons/logo.png")
        self.setWindowIcon(self.icon)
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Controllers ka instance
        self.login = LoginController(self)
        self.signup = SignupController(self)

        # Sare pages ko add kr diya
        self.stack.addWidget(self.login)
        self.stack.addWidget(self.signup)
        self.stack.setCurrentWidget(self.login)

    def showLogin(self):
        self.setMinimumSize(850, 580)
        self.resize(850, 580)
        self.stack.setCurrentWidget(self.login)

    def showSignup(self):
        self.setMinimumSize(850, 580)
        self.resize(850, 580)
        self.stack.setCurrentWidget(self.signup)

    def showHome(self, user):
        self.home = HomeController(self, user)
        self.stack.addWidget(self.home)
        self.setMinimumSize(1000, 580)
        self.resize(1200, 720)
        self.centerWindow()
        self.stack.setCurrentWidget(self.home)

    def centerWindow(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


def main():
    # Initiate database
    init_db()
    # Main window ka UI
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
