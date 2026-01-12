from PySide6.QtWidgets import QWidget

from ui.test_result_student_row import Ui_student_test_card


class StudentTestRowController(QWidget):
    def __init__(self, test_data):

        super().__init__()
        self.ui = Ui_student_test_card()
        self.ui.setupUi(self)

        self.populate_data(test_data)

    def populate_data(self, data):
        name, date, max_m, pass_m, obtained = data

        self.ui.lbl_name.setText(name)
        self.ui.lbl_date.setText(date if date else "N/A")
        self.ui.lbl_max.setText(str(max_m))
        self.ui.lbl_pass.setText(str(pass_m))

        if obtained is not None:
            self.ui.lbl_score.setText(str(int(obtained)))

            if obtained >= pass_m:
                self.set_status("PASS", "#E0F2F1", "#009688")  # Green
            else:
                self.set_status("FAIL", "#FFEBEE", "#D32F2F")  # Red
        else:
            self.ui.lbl_score.setText("-")
            self.set_status("ABSENT", "#F5F5F5", "#9E9E9E")  # Grey

    def set_status(self, text, bg_color, text_color):
        self.ui.lbl_status.setText(text)
        self.ui.lbl_status.setStyleSheet(
            f"""
            background-color: {bg_color}; 
            color: {text_color}; 
            border-radius: 4px; 
            font-weight: bold; 
            font-size: 11px;
        """
        )
