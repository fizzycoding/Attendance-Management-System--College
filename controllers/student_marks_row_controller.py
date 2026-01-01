from PySide6.QtWidgets import QFrame

from ui.components.student_marks_row import Ui_student_marks_row


class StudentMarksRowController(QFrame, Ui_student_marks_row):
    def __init__(self, sNo, name, member_id, marks, max_marks, passing_marks):
        super().__init__()
        self.setupUi(self)

        self.member_id = member_id
        self.passing_marks = int(passing_marks)

        self.serial_no.setText(str(sNo))
        self.student_name.setText(name)

        self.input_marks.setMaximum(int(max_marks))
        self.btn_status.clicked.connect(self.toggleAbsent)
        if marks is None:
            self.input_marks.setValue(0)
            self.setStatus("Not Attempted")
        else:
            val = int(marks)
            self.input_marks.setValue(val)
            self.updateStatusLogic(val)

        self.input_marks.valueChanged.connect(self.updateStatusLogic)

    def updateStatusLogic(self, value):
        if value >= self.passing_marks:
            self.setStatus("Pass")
        else:
            self.setStatus("Fail")

    def setStatus(self, status):
        self.btn_status.setText(status)

        if status == "Pass":
            self.btn_status.setStyleSheet("""
                background-color: rgb(184, 242, 210); 
                color: #009688;
                font-weight: bold;
                font-size: 11px;""")
        elif status == "Fail":
            self.btn_status.setStyleSheet("""
                background-color: rgb(255, 202, 210); 
                color: #D32F2F; 
                font-weight: bold;
                font-size: 11px;""")
        else:
            self.btn_status.setStyleSheet("""
                background-color: rgb(220, 220, 220);
                color: rgb(104, 104, 104);
                font-weight: bold;
                font-size: 11px;""")

    def isAttempted(self):
        return self.btn_status.text() != "Not Attempted"

    def getMarks(self):
        return self.input_marks.value()

    def toggleAbsent(self):
        if self.btn_status.text() != "Not Attempted":
            self.setStatus("Not Attempted")
            self.input_marks.setValue(0)
        else:
            self.updateStatusLogic(self.input_marks.value())
