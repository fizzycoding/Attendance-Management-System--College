from PySide6.QtWidgets import QWidget

from database.database import getDB
from ui.login_ui import Ui_login_form_main_window


class LoginController(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow
        self.ui = Ui_login_form_main_window()
        self.ui.setupUi(self)
        self.ui.loginButton.clicked.connect(self.handleLogin)
        self.ui.signupButton.clicked.connect(self.switchToSignUp)
        self.ui.passwordInputBox.returnPressed.connect(self.handleLogin)

    def handleLogin(self):
        username = self.ui.usernameInputBox.text().strip().lower()
        password = self.ui.passwordInputBox.text().strip()

        if not self.validateLogin():
            return None

        db = getDB()
        cursor = db.cursor()
        try:
            query = "SELECT id, name, username, role, created_at FROM users WHERE username = ? AND password = ?"
            cursor.execute(query, (username, password))

            user = cursor.fetchone()
            if not user:
                self.setError("Invalid credentials")
                return None

            self.loginSuccess(user)

        except Exception as e:
            # --------- SIGNUP Failed ----------
            db.rollback()
            self.setError("Failed to login")
            print(f"Database error {e}")
        finally:
            cursor.close()
            db.close()
        return None

    def validateLogin(self):
        username = self.ui.usernameInputBox.text()
        password = self.ui.passwordInputBox.text()
        if len(username.strip()) <= 0:
            self.setError("Username is empty")
            return False
        elif len(password.strip()) <= 0:
            self.setError("Password is empty")
            return False
        else:
            self.setError("")
        return True

    def switchToSignUp(self):
        self.mainWindow.showSignup()

    def setError(self, errorMessage):
        error = self.ui.erroLabel
        error.setText(errorMessage)

    def loginSuccess(self, user):
        self.mainWindow.showHome(user)
