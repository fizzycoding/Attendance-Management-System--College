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
        else:
            self.attendance_rate_label.setText("00%")
            self.progressBar_attendance_rate.setValue(0)

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
