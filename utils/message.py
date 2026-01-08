from PySide6.QtWidgets import QMessageBox


def showMessage(self, title, message, icon=QMessageBox.Icon.Information):
    msgBox = QMessageBox(self)
    msgBox.setWindowTitle(title)
    msgBox.setText(message)
    msgBox.setIcon(icon)

    # Force White BG and Black Text for everything inside
    msgBox.setStyleSheet("""
        QMessageBox {
            background-color: white;
            color: black;
        }
        QLabel {
            color: black;
            background-color: transparent; /* Fixes label having wrong bg */
        }
        QPushButton {
            color: black;
            background-color: #f0f0f0;
            border: 1px solid #ccc;
            padding: 5px 15px;
            border-radius: 4px;
        }
        QPushButton:hover {
            background-color: #e0e0e0;
        }
    """)
    msgBox.exec()


def showQuestionMessage(self, title, message):
    msgBox = QMessageBox(self)
    msgBox.setWindowTitle(title)
    msgBox.setText(message)
    msgBox.setIcon(QMessageBox.Icon.Question)
    msgBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    msgBox.setDefaultButton(QMessageBox.StandardButton.Yes)

    # Same stylesheet for consistency
    msgBox.setStyleSheet("""
        QMessageBox {
            background-color: white;
            color: black;
        }
        QLabel {
            color: black;
            background-color: transparent;
        }
        QPushButton {
            color: black;
            background-color: #f0f0f0;
            border: 1px solid #ccc;
            padding: 5px 15px;
            border-radius: 4px;
        }
        QPushButton:hover {
            background-color: #e0e0e0;
        }
    """)
    return msgBox.exec()
