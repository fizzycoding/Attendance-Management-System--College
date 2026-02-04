from PySide6.QtCore import QDate
from PySide6.QtWidgets import QDialog

from ui.components.export_report_popup import Ui_ExportReportPopup


class ExportReportPopupController(QDialog):
    def __init__(self, className, parent=None):
        super().__init__(parent)
        self.ui = Ui_ExportReportPopup()
        self.ui.setupUi(self)
        self.ui.label_class_name.setText(className)

        currentDate = QDate.currentDate()
        self.ui.date_from.setDate(QDate(currentDate.year(), 1, 1))
        self.ui.date_to.setDate(QDate(currentDate.year(), 1, 31))

        self.ui.btn_close.clicked.connect(self.reject)
        self.ui.btn_excel.clicked.connect(self.onExcelClicked)

        self.export_action = None

    def onExcelClicked(self):
        self.export_action = "excel"
        self.accept()

    def getExportData(self):
        return {
            "action": self.export_action,
            "from_date": self.ui.date_from.date().toString("yyyy-MM-dd"),
            "to_date": self.ui.date_to.date().toString("yyyy-MM-dd"),
            "include_attendance": self.ui.check_attendance.isChecked(),
            "include_tests": self.ui.check_tests.isChecked(),
            "include_fees": self.ui.check_fees.isChecked()
        }
