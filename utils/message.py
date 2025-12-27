from PySide6.QtWidgets import QMessageBox


def showMessage(self, title, message, icon=QMessageBox.Icon.Information):
    msgBox = QMessageBox(self)
    msgBox.setWindowTitle(title)
    msgBox.setText(message)
    msgBox.setIcon(icon)
    msgBox.setStyleSheet("QLabel{color:black;}QPushButton{color:black;}")
    msgBox.exec()


def showQuestionMessage(self, title, message):
    # 1. Create the object manually
    msgBox = QMessageBox(self)
    msgBox.setWindowTitle(title)
    msgBox.setText(message)
    msgBox.setIcon(QMessageBox.Icon.Question)
    msgBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    msgBox.setDefaultButton(QMessageBox.StandardButton.Yes)
    msgBox.setStyleSheet("QLabel{color:black;}QPushButton{color:black;}")
    return msgBox.exec()
