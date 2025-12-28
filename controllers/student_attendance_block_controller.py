from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QFrame

from ui.components.student_attendance_block import Ui_student_block
from utils.constants import ATTENDANCE_STATUS


class StudentAttendanceBlockController(QFrame, Ui_student_block):
    attendanceChanged = Signal(int, str)

    def __init__(self, id, sNo, name, member_id, attendanceRate=0, status=None):
        super().__init__()
        self.setupUi(self)
        self.id = id
        self.member_id = member_id
        self.serial_number.setText(str(sNo))
        self.name.setText(name)

        self.presentUncheckedIcon = QIcon("icons/present_unchecked.png")
        self.presentIcon = QIcon("icons/present.png")
        self.absentUncheckedIcon = QIcon("icons/absent_unchecked.png")
        self.absentIcon = QIcon("icons/absent.png")

        if attendanceRate:
            self.attendance_rate_label.setText(f"{round(attendanceRate)}%")
            self.progressBar_attendance_rate.setValue(round(attendanceRate))
            self.colorProgressBar(round(attendanceRate))
        else:
            self.attendance_rate_label.setText("00%")
            self.progressBar_attendance_rate.setValue(0)
            self.colorProgressBar(0)

        self.btn_present.setIcon(self.presentUncheckedIcon)
        self.btn_absent.setIcon(self.absentUncheckedIcon)
        if status == ATTENDANCE_STATUS.PRESENT:
            self.btn_present.setIcon(self.presentIcon)
        elif status == ATTENDANCE_STATUS.ABSENT:
            self.btn_absent.setIcon(self.absentIcon)

        self.btn_present.clicked.connect(lambda: self.handleMarkAttendance(ATTENDANCE_STATUS.PRESENT))
        self.btn_absent.clicked.connect(lambda: self.handleMarkAttendance(ATTENDANCE_STATUS.ABSENT))

    def handleMarkAttendance(self, status):
        if status == ATTENDANCE_STATUS.PRESENT:
            self.btn_absent.setIcon(self.absentUncheckedIcon)
            self.btn_present.setIcon(self.presentIcon)
        elif status == ATTENDANCE_STATUS.ABSENT:
            self.btn_present.setIcon(self.presentUncheckedIcon)
            self.btn_absent.setIcon(self.absentIcon)
        self.attendanceChanged.emit(self.member_id, status)

    def colorProgressBar(self, rate):
        # 1. Determine the color based on the rate
        if rate >= 75:
            color = "#4CAF50"  # Green
        elif rate >= 50:
            color = "#FF9800"  # Orange
        else:
            color = "#F44336"  # Red

        self.progressBar_attendance_rate.setStyleSheet(f"""
            QProgressBar::chunk {{
                background-color: {color};
            }}
        """)
