from PySide6.QtWidgets import QMessageBox


def showMessage(self, title, message, icon=QMessageBox.Icon.Information):
    msgBox = QMessageBox(self)
    msgBox.setWindowTitle(title)
    msgBox.setText(message)
    msgBox.setIcon(icon)
    msgBox.setStyleSheet("QLabel{color:black;}QPushButton{color:black;}")
    msgBox.exec()
