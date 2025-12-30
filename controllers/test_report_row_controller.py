from PySide6.QtWidgets import QFrame, QVBoxLayout
from ui.components.test_report_row import Ui_test_report_row
from ui.components.gradient_chart import GradientDonutChart


class TestReportRowController(QFrame, Ui_test_report_row):
    def __init__(self, name, marks_obtained, max_marks, passing_marks):
        super().__init__()
        self.setupUi(self)

        # 1. Set Text Info
        self.test_name.setText(name)
        self.marks_label.setText(f"{int(marks_obtained)}/{max_marks}")
        self.passing_label.setText(f"Min: {passing_marks}")

        # 2. Create the Custom Chart
        self.chart = GradientDonutChart()
        self.chart.setValues(marks_obtained, max_marks)

        # 3. Add to the UI Container
        # The 'chart_container' is the empty QFrame in your .ui file.
        # We need to give it a layout so the chart fits inside.
        if self.chart_container.layout() is None:
            layout = QVBoxLayout(self.chart_container)
            layout.setContentsMargins(0, 0, 0, 0)  # Remove margins so chart fills the box
            self.chart_container.setLayout(layout)
        else:
            layout = self.chart_container.layout()

        layout.addWidget(self.chart)

        # 4. Force visibility (just in case)
        self.chart.show()