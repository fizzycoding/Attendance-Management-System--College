from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPen, QColor, QConicalGradient, QFont
from PySide6.QtCore import Qt, QRectF


class GradientDonutChart(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.value = 0
        self.max_value = 100
        self.percentage_text = "0%"

        self.setMinimumSize(60, 60)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

    def setValues(self, value, max_value):
        self.value = value
        self.max_value = max_value

        if self.max_value > 0:
            percent = int((self.value / self.max_value) * 100)
        else:
            percent = 0
        self.percentage_text = f"{percent}%"
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        side = min(self.width(), self.height())
        margin = 3
        x_offset = (self.width() - side) / 2 + margin
        y_offset = (self.height() - side) / 2 + margin
        rect_side = side - 2 * margin
        rect = QRectF(x_offset, y_offset, rect_side, rect_side)

        startAngle = 225 * 16
        spanAngle = -270 * 16

        bg_pen = QPen(QColor(235, 235, 235), 6)
        bg_pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        painter.setPen(bg_pen)
        painter.drawArc(rect, startAngle, spanAngle)

        if self.max_value > 0:
            percentage = self.value / self.max_value
        else:
            percentage = 0

        if percentage > 1.0: percentage = 1.0

        progressSpan = spanAngle * percentage

        gradient = QConicalGradient(rect.center(), 270)
        gradient.setColorAt(0.0, QColor("#00E676"))
        gradient.setColorAt(0.5, QColor("#FFD740"))
        gradient.setColorAt(1.0, QColor("#FF5252"))

        progress_pen = QPen(Qt.BrushStyle.NoBrush, 6)
        progress_pen.setBrush(gradient)
        progress_pen.setCapStyle(Qt.PenCapStyle.RoundCap)

        painter.setPen(progress_pen)
        painter.drawArc(rect, startAngle, progressSpan)

        painter.setPen(QColor("#333333"))
        font = QFont("Segoe UI", 11, QFont.Weight.Bold)
        painter.setFont(font)
        painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, self.percentage_text)

        painter.end()