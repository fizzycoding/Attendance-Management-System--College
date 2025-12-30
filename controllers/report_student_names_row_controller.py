from PySide6.QtCore import Signal
from PySide6.QtWidgets import QFrame

from ui.components.report_student_names_row import Ui_reportStudentNameRow


class ReportStudentNamesRowController(QFrame, Ui_reportStudentNameRow):
    clicked = Signal(int)

    def __init__(self, memberId, studentId, sNo, name, attendanceRate):
        super().__init__()
        self.setupUi(self)
        self.memberId = memberId
        self.studentId = studentId
        self.sNumber.setText(str(sNo))
        self.name.setText(name)
        self.rate.setText(f"{attendanceRate}%")

    def mousePressEvent(self, event):
        self.clicked.emit(self.memberId)

    def setSelected(self, selected: bool):
        if selected:
            # Highlight Color (Light Green/Teal to match your theme)
            self.setStyleSheet("""
                QFrame {
                    background-color: #E0F2F1; 
                    border-left: 4px solid #009688;
                }
                QLabel { background-color: transparent;border-left: none; }
            """)
        else:
            # Default White style (Reset)
            self.setStyleSheet("""
                QFrame {
                    background-color: transparent; 
                    border-left: none;
                    border-left: 4px solid transparent;
                }
                QLabel { background-color: transparent; }
            """)
