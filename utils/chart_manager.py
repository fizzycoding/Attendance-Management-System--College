from PySide6.QtCharts import QChart, QChartView, QPieSeries, QLineSeries, QBarSeries, QBarSet, QBarCategoryAxis, \
    QValueAxis
from PySide6.QtCore import Qt, QMargins
from PySide6.QtGui import QPainter, QColor, QPen, QCursor
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

    # --- 1. DONUT CHART ---
    def createPieChart(self, present, absent, total):
        series = QPieSeries()
        series.setHoleSize(0.5)

        def add_slice(label, value, color):
            _slice = series.append(label, value)
            _slice.setColor(color)
            _slice.setBorderColor(color)
            # Hover Event
            _slice.hovered.connect(lambda state, s=_slice: self._on_pie_hover(state, s))
            return _slice

        add_slice("Present", present, self.COLOR_PRESENT)
        add_slice("Absent", absent, self.COLOR_ABSENT)

        not_marked = total - (present + absent)
        if not_marked > 0:
            s = add_slice("Not Marked", not_marked, self.COLOR_OTHER)
            s.setLabelVisible(False)  # Hide label for grey area to keep it clean

        chart = QChart()
        chart.addSeries(series)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignmentFlag.AlignBottom)
        chart.legend().setFont(self._get_font(10))

        chart.setBackgroundVisible(False)
        chart.setMargins(QMargins(0, 0, 0, 0))  # Tight margins

        return self._create_chart_view(chart)

    # --- 2. WEEKLY LINE CHART (Fixed) ---
    def createWeeklyLineChart(self, present_data, absent_data):
        series_p = QLineSeries()
        series_p.setName("Present")
        pen_p = QPen(self.COLOR_PRESENT)
        pen_p.setWidth(3)
        series_p.setPen(pen_p)

        series_a = QLineSeries()
        series_a.setName("Absent")
        pen_a = QPen(self.COLOR_ABSENT)
        pen_a.setWidth(3)
        series_a.setPen(pen_a)

        max_value = 0
        days_count = max(len(present_data), len(absent_data))

        for i in range(days_count):
            p_val = present_data[i] if i < len(present_data) else 0
            a_val = absent_data[i] if i < len(absent_data) else 0

            series_p.append(i, p_val)
            series_a.append(i, a_val)

            # Track max for Axis scaling
            max_value = max(max_value, p_val, a_val)

        # 2. Add Tooltips
        series_p.hovered.connect(lambda point, state: self._on_line_hover(point, state, "Present"))
        series_a.hovered.connect(lambda point, state: self._on_line_hover(point, state, "Absent"))

        # 3. Create Chart
        chart = QChart()
        chart.addSeries(series_p)
        chart.addSeries(series_a)
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignmentFlag.AlignTop)
        chart.setBackgroundVisible(False)

        # Reduce margins so it fills the widget
        chart.layout().setContentsMargins(0, 0, 0, 0)
        chart.setMargins(QMargins(0, 0, 0, 0))

        # 4. Axes
        axis_x = QBarCategoryAxis()
        axis_x.append(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
        axis_x.setGridLineVisible(False)
        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        series_p.attachAxis(axis_x)
        series_a.attachAxis(axis_x)

        # 5. Smart Y-Axis Scaling (The logic you asked for)
        # Round up to nearest 5
        remainder = max_value % 5
        if remainder != 0:
            max_value = max_value + (5 - remainder)

        # Add ONE extra buffer step (e.g. if max is 20, make axis 25)
        top_bound = max_value + 5

        axis_y = QValueAxis()
        axis_y.setRange(0, top_bound)  # Set explicit range
        axis_y.setTickCount(int(top_bound / 5) + 1)  # Ensure ticks are at 0, 5, 10...
        axis_y.setLabelFormat("%d")  # Integer format
        axis_y.setGridLineVisible(True)
        axis_y.setGridLineColor(QColor("#f0f0f0"))

        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)
        series_p.attachAxis(axis_y)
        series_a.attachAxis(axis_y)

        return self._create_chart_view(chart)

    # --- 3. MONTHLY BAR CHART ---
    def createMonthlyBarChart(self, data_dict):
        set_present = QBarSet("Present")
        set_absent = QBarSet("Absent")

        set_present.setColor(self.COLOR_PRESENT)
        set_absent.setColor(self.COLOR_ABSENT)
        set_present.setBorderColor(Qt.GlobalColor.transparent)
        set_absent.setBorderColor(Qt.GlobalColor.transparent)

        set_present.hovered.connect(lambda status, index: self._on_bar_hover(status, index, set_present))
        set_absent.hovered.connect(lambda status, index: self._on_bar_hover(status, index, set_absent))

        categories = []
        max_val = 0

        for month, values in data_dict.items():
            categories.append(month)
            p_val = values[0]
            a_val = values[1]
            set_present.append(p_val)
            set_absent.append(a_val)
            max_val = max(max_val, p_val, a_val)

        series = QBarSeries()
        series.append(set_present)
        series.append(set_absent)
        series.setBarWidth(0.6)

        chart = QChart()
        chart.addSeries(series)
        chart.setBackgroundVisible(False)
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignmentFlag.AlignTop)
        chart.setMargins(QMargins(0, 0, 0, 0))

        axis_x = QBarCategoryAxis()
        axis_x.append(categories)
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

    # --- HOVER EVENTS ---
    def _on_pie_hover(self, state, _slice):
        if state:
            QToolTip.showText(QCursor.pos(), f"{_slice.label()}: {int(_slice.value())}")
        else:
            QToolTip.hideText()

    def _on_line_hover(self, point, state, name):
        if state:
            QToolTip.showText(QCursor.pos(), f"{name}: {int(point.y())}")
        else:
            QToolTip.hideText()

    def _on_bar_hover(self, status, index, bar_set):
        if status:
            val = bar_set.at(index)
            QToolTip.showText(QCursor.pos(), f"{bar_set.label()}: {int(val)}")
        else:
            QToolTip.hideText()

    def _get_font(self, size):
        from PySide6.QtGui import QFont
        f = QFont("Segoe UI", size)
        f.setBold(True)
        return f
