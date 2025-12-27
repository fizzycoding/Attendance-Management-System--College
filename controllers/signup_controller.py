from PySide6.QtWidgets import QWidget

from database.database import getDB
from ui.signup_ui import Ui_signup_form_main_window
from utils.constants import ROLE


class SignupController(QWidget):
    def __init__(self, mainWindow):
        super().__init__()

        self.mainWindow = mainWindow

        self.ui = Ui_signup_form_main_window()
        self.ui.setupUi(self)

        self.ui.registerButton.clicked.connect(self.handle_signup)
        self.ui.switchLoginButton.clicked.connect(self.switchToLogin)

    def handle_signup(self):
        name = self.ui.nameInputBox.text().strip()
        username = self.ui.usernameInputBox.text().strip().lower()
        password = self.ui.passwordInputBox.text().strip()
        if self.ui.teacherRadioButton.isChecked():
            role = "teacher"
        else:
            role = "student"

        if not self.validateSignup():
            return

        # --------- SIGNUP DATABASE ----------
        db = getDB()
        cursor = db.cursor()
        try:
            query = "SELECT 1 FROM users WHERE username = ? LIMIT 1"
            cursor.execute(query, (username,))
            if cursor.fetchone():
                self.setError("Username already taken!")
                return
            else:
                insertQuery = "INSERT INTO users(name, username, password, role) VALUES (?, ?, ?, ?)"
                userData = (name, username, password, role)
                cursor.execute(insertQuery, userData)
                id = cursor.lastrowid
                db.commit()

                cursor.execute(
                    "SELECT id, name, username, role, created_at  FROM users WHERE id = ?",
                    (id,),
                )
                newUserData = cursor.fetchone()
                self.signupSuccess(newUserData)
                # --------- SIGNUP SUCCESS ----------
        except Exception as e:
            # --------- SIGNUP Failed ----------
            db.rollback()
            self.setError("Failed to create account")
            print(f"Database error {e}")
            return None
        finally:
            cursor.close()
            db.close()

    def validateSignup(self):
        name = self.ui.nameInputBox.text()
        username = self.ui.usernameInputBox.text()
        password = self.ui.passwordInputBox.text()
        role = None
        if self.ui.teacherRadioButton.isChecked():
            role = ROLE.TEACHER
        else:
            role = ROLE.STUDENT

        # Basic empty input validation

        if len(name.strip()) <= 0:
            self.setError("Name is empty")
            return False
        elif len(username.strip()) <= 0:
            self.setError("Username is empty")
            return False
        elif len(password.strip()) <= 0:
            self.setError("Password is empty")
            return False
        elif role not in (ROLE.STUDENT, ROLE.TEACHER):
            self.setError("Invalid role")
            return False
        else:
            self.setError("")
        return True

    def switchToLogin(self):
        self.mainWindow.showLogin()

    def setError(self, errorMessage):
        error = self.ui.erroLabel
        error.setText(errorMessage)

    def signupSuccess(self, user):
        self.mainWindow.showHome(user)
