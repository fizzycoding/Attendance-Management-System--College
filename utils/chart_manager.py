from PySide6.QtCharts import QChart, QChartView, QPieSeries, QBarSeries, QBarSet, QBarCategoryAxis, QValueAxis
from PySide6.QtCore import Qt, QMargins
from PySide6.QtGui import QPainter, QColor, QCursor
from PySide6.QtWidgets import QToolTip, QSizePolicy


class ChartManager:
    def __init__(self):
        self.COLOR_PRESENT = QColor("#2ab79d")  # Teal
        self.COLOR_ABSENT = QColor("#ff5252")  # Red
        self.COLOR_OTHER = QColor("#e0e0e0")  # Grey

    def _create_chart_view(self, chart):
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        chart_view.setStyleSheet("background: transparent; border: none;")
        chart_view.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        return chart_view

    def _get_font(self, size):
        from PySide6.QtGui import QFont
        f = QFont("Segoe UI", size)
        f.setBold(True)
        return f

    def createPieChart(self, present, absent, total):
        series = QPieSeries()
        series.setHoleSize(0.5)

        def add_slice(label, value, color):
            _slice = series.append(label, value)
            _slice.setColor(color)
            _slice.setBorderColor(color)
            _slice.hovered.connect(lambda state, s=_slice: self._on_pie_hover(state, s))
            return _slice

        add_slice("Present", present, self.COLOR_PRESENT)
        add_slice("Absent", absent, self.COLOR_ABSENT)

        not_marked = total - (present + absent)
        if not_marked > 0:
            s = add_slice("Not Marked", not_marked, self.COLOR_OTHER)
            s.setLabelVisible(False)

        chart = QChart()
        chart.addSeries(series)
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignmentFlag.AlignBottom)
        chart.legend().setFont(self._get_font(10))
        chart.setBackgroundVisible(False)
        chart.setMargins(QMargins(0, 0, 0, 0))

        return self._create_chart_view(chart)

    def createWeeklyBarChart(self, present_data, absent_data):
        set_present = QBarSet("Present")
        set_absent = QBarSet("Absent")

        set_present.setColor(self.COLOR_PRESENT)
        set_absent.setColor(self.COLOR_ABSENT)

        set_present.setBorderColor(Qt.GlobalColor.transparent)
        set_absent.setBorderColor(Qt.GlobalColor.transparent)

        max_val = 0
        for p, a in zip(present_data, absent_data):
            set_present.append(p)
            set_absent.append(a)
            max_val = max(max_val, p, a)

        set_present.hovered.connect(lambda status, index: self._on_bar_hover(status, index, set_present))
        set_absent.hovered.connect(lambda status, index: self._on_bar_hover(status, index, set_absent))

        series = QBarSeries()
        series.append(set_present)
        series.append(set_absent)
        series.setBarWidth(0.8)

        chart = QChart()
        chart.addSeries(series)
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignmentFlag.AlignTop)
        chart.legend().setFont(self._get_font(9))
        chart.setBackgroundVisible(False)
        chart.setMargins(QMargins(0, 0, 0, 0))

        axis_x = QBarCategoryAxis()
        axis_x.append(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
        axis_x.setGridLineVisible(False)
        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        series.attachAxis(axis_x)

        remainder = max_val % 5
        if remainder != 0: max_val += (5 - remainder)
        top_bound = max_val + 5

        axis_y = QValueAxis()
        axis_y.setRange(0, top_bound)
        axis_y.setTickCount(int(top_bound / 5) + 1)
        axis_y.setLabelFormat("%d")
        axis_y.setGridLineVisible(True)
        axis_y.setGridLineColor(QColor("#f0f0f0"))

        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)
        series.attachAxis(axis_y)

        return self._create_chart_view(chart)

    def _on_pie_hover(self, state, _slice):
        if state:
            QToolTip.showText(QCursor.pos(), f"{_slice.label()}: {int(_slice.value())}")
        else:
            QToolTip.hideText()

    def _on_bar_hover(self, status, index, bar_set):
        if status:
            val = bar_set.at(index)
            QToolTip.showText(QCursor.pos(), f"{bar_set.label()}: {int(val)}")
        else:
            QToolTip.hideText()
