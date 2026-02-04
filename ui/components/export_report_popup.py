from PySide6.QtCore import (QCoreApplication, QDate, QMetaObject, Qt)
from PySide6.QtGui import (QCursor)
from PySide6.QtWidgets import (QCheckBox, QDateEdit, QFrame, QGroupBox, QHBoxLayout, QLabel,
                               QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
                               QWidget)


class Ui_ExportReportPopup(object):
    def setupUi(self, ExportReportPopup):
        if not ExportReportPopup.objectName():
            ExportReportPopup.setObjectName(u"ExportReportPopup")
        ExportReportPopup.resize(500, 492)
        ExportReportPopup.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(ExportReportPopup)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.backgroundFrame = QFrame(ExportReportPopup)
        self.backgroundFrame.setObjectName(u"backgroundFrame")
        self.backgroundFrame.setStyleSheet(u"#backgroundFrame {\n"
                                           "    background-color: white;\n"
                                           "}\n"
                                           "QLabel {\n"
                                           "    color: #333;\n"
                                           "    font-family: \"Segoe UI\";\n"
                                           "    font-size: 14px;\n"
                                           "    font-weight: 600;\n"
                                           "    border: none; \n"
                                           "}\n"
                                           "#label_class_name {\n"
                                           "    color: #3388FF;\n"
                                           "    font-size: 16px;\n"
                                           "    font-weight: 700;\n"
                                           "}\n"
                                           "\n"
                                           "/* Checkbox Style */\n"
                                           "QCheckBox {\n"
                                           "    font-family: \"Segoe UI\";\n"
                                           "    font-size: 14px;\n"
                                           "    color: #333;\n"
                                           "    spacing: 8px;\n"
                                           "}\n"
                                           "QCheckBox::indicator {\n"
                                           "    width: 20px;\n"
                                           "    height: 20px;\n"
                                           "    border: 1px solid #999;\n"
                                           "    border-radius: 4px;\n"
                                           "    background: white;\n"
                                           "}\n"
                                           "QCheckBox::indicator:checked {\n"
                                           "    background-color: #3388FF;\n"
                                           "    border: 1px solid #3388FF;\n"
                                           "    image: url(icons/checked.png); /* Ensure you handle the icon or remove this line if strictly relying on color */\n"
                                           "}\n"
                                           "\n"
                                           "/* General Input Style */\n"
                                           "QDateEdit {\n"
                                           "    height: 35px;\n"
                                           "    padding: 0 10px;\n"
                                           "    font-family: \"Segoe UI\";\n"
                                           "    font-size: 14px;\n"
                                           " "
                                           "   color: #111;\n"
                                           "    border: 1px solid rgb(150, 150, 150);\n"
                                           "    background: #fff;\n"
                                           "    border-radius: 4px;\n"
                                           "}\n"
                                           "QDateEdit:focus {\n"
                                           "    border: 1.5px solid #3388FF;\n"
                                           "}\n"
                                           "QCalendarWidget QWidget { background-color: white; color: black; }\n"
                                           "QCalendarWidget QAbstractItemView:enabled { \n"
                                           "    color: black; \n"
                                           "    selection-background-color: #3388FF; \n"
                                           "    selection-color: white;\n"
                                           "}\n"
                                           "QCalendarWidget QToolButton { color: black; icon-size: 25px; }\n"
                                           "QCalendarWidget QSpinBox { background-color: white; color: black; }\n"
                                           "\n"
                                           "QPushButton {\n"
                                           "    height: 40px;\n"
                                           "    padding: 0 16px;\n"
                                           "    border: none;\n"
                                           "    border-radius: 5px;\n"
                                           "    font-family: \"Segoe UI\";\n"
                                           "    font-size: 14px;\n"
                                           "    font-weight: 700;\n"
                                           "    color: white;\n"
                                           "}\n"
                                           "\n"
                                           "#btn_excel {\n"
                                           "    background-color: #3388FF;\n"
                                           "}\n"
                                           "#btn_excel:hover { background-color: #0055FF; }\n"
                                           "\n"
                                           "#btn_close {\n"
                                           "    background-color: transparent;\n"
                                           "    color: #555;\n"
                                           "    border: 1px solid #ccc;\n"
                                           "}\n"
                                           ""
                                           "#btn_close:hover { background-color: #f0f0f0; }\n"
                                           "")
        self.backgroundFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.backgroundFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.backgroundFrame)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(25, 25, 25, 25)
        self.label_title = QLabel(self.backgroundFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setStyleSheet(u"font-size: 22px; font-weight: 800; color: #333; margin-bottom: 5px;")
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_title)

        self.label_class_name = QLabel(self.backgroundFrame)
        self.label_class_name.setObjectName(u"label_class_name")
        self.label_class_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_class_name)

        self.verticalSpacer_top = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_top)

        self.group_date = QGroupBox(self.backgroundFrame)
        self.group_date.setObjectName(u"group_date")
        self.group_date.setStyleSheet(u"QGroupBox{border:none;}")
        self.horizontalLayout_dates = QHBoxLayout(self.group_date)
        self.horizontalLayout_dates.setSpacing(15)
        self.horizontalLayout_dates.setObjectName(u"horizontalLayout_dates")
        self.horizontalLayout_dates.setContentsMargins(0, -1, 0, -1)
        self.layout_from = QVBoxLayout()
        self.layout_from.setSpacing(5)
        self.layout_from.setObjectName(u"layout_from")
        self.label_from = QLabel(self.group_date)
        self.label_from.setObjectName(u"label_from")

        self.layout_from.addWidget(self.label_from)

        self.date_from = QDateEdit(self.group_date)
        self.date_from.setObjectName(u"date_from")
        self.date_from.setCalendarPopup(True)
        self.date_from.setDate(QDate(2025, 1, 1))

        self.layout_from.addWidget(self.date_from)

        self.horizontalLayout_dates.addLayout(self.layout_from)

        self.layout_to = QVBoxLayout()
        self.layout_to.setSpacing(5)
        self.layout_to.setObjectName(u"layout_to")
        self.label_to = QLabel(self.group_date)
        self.label_to.setObjectName(u"label_to")

        self.layout_to.addWidget(self.label_to)

        self.date_to = QDateEdit(self.group_date)
        self.date_to.setObjectName(u"date_to")
        self.date_to.setCalendarPopup(True)
        self.date_to.setDate(QDate(2025, 12, 31))

        self.layout_to.addWidget(self.date_to)

        self.horizontalLayout_dates.addLayout(self.layout_to)

        self.verticalLayout_2.addWidget(self.group_date)

        self.verticalSpacer_mid = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_mid)

        self.widget_checks = QWidget(self.backgroundFrame)
        self.widget_checks.setObjectName(u"widget_checks")
        self.verticalLayout_checks = QVBoxLayout(self.widget_checks)
        self.verticalLayout_checks.setSpacing(12)
        self.verticalLayout_checks.setObjectName(u"verticalLayout_checks")
        self.verticalLayout_checks.setContentsMargins(10, -1, -1, -1)
        self.label_include = QLabel(self.widget_checks)
        self.label_include.setObjectName(u"label_include")
        self.label_include.setStyleSheet(u"color: #777; font-weight: normal; margin-bottom: 5px;")

        self.verticalLayout_checks.addWidget(self.label_include)

        self.check_attendance = QCheckBox(self.widget_checks)
        self.check_attendance.setObjectName(u"check_attendance")
        self.check_attendance.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.check_attendance.setChecked(True)

        self.verticalLayout_checks.addWidget(self.check_attendance)

        self.check_tests = QCheckBox(self.widget_checks)
        self.check_tests.setObjectName(u"check_tests")
        self.check_tests.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.check_tests.setChecked(True)

        self.verticalLayout_checks.addWidget(self.check_tests)

        self.check_fees = QCheckBox(self.widget_checks)
        self.check_fees.setObjectName(u"check_fees")
        self.check_fees.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.check_fees.setChecked(True)

        self.verticalLayout_checks.addWidget(self.check_fees)

        self.verticalLayout_2.addWidget(self.widget_checks)

        self.verticalSpacer_bottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_bottom)

        self.horizontalLayout_actions = QHBoxLayout()
        self.horizontalLayout_actions.setSpacing(10)
        self.horizontalLayout_actions.setObjectName(u"horizontalLayout_actions")
        self.btn_close = QPushButton(self.backgroundFrame)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_actions.addWidget(self.btn_close)

        self.btn_excel = QPushButton(self.backgroundFrame)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_actions.addWidget(self.btn_excel)

        self.verticalLayout_2.addLayout(self.horizontalLayout_actions)

        self.verticalLayout.addWidget(self.backgroundFrame)

        self.retranslateUi(ExportReportPopup)

        QMetaObject.connectSlotsByName(ExportReportPopup)

    # setupUi

    def retranslateUi(self, ExportReportPopup):
        ExportReportPopup.setWindowTitle(QCoreApplication.translate("ExportReportPopup", u"Export Reports", None))
        self.label_title.setText(QCoreApplication.translate("ExportReportPopup", u"Export Data", None))
        self.label_class_name.setText(
            QCoreApplication.translate("ExportReportPopup", u"Class: Class X - Science", None))
        self.label_from.setText(QCoreApplication.translate("ExportReportPopup", u"From Month", None))
        self.date_from.setDisplayFormat(QCoreApplication.translate("ExportReportPopup", u"MMM yyyy", None))
        self.label_to.setText(QCoreApplication.translate("ExportReportPopup", u"To Month", None))
        self.date_to.setDisplayFormat(QCoreApplication.translate("ExportReportPopup", u"MMM yyyy", None))
        self.label_include.setText(QCoreApplication.translate("ExportReportPopup", u"Include in Report:", None))
        self.check_attendance.setText(QCoreApplication.translate("ExportReportPopup", u"Attendance Records", None))
        self.check_tests.setText(QCoreApplication.translate("ExportReportPopup", u"Test Results", None))
        self.check_fees.setText(QCoreApplication.translate("ExportReportPopup", u"Fees Payments", None))
        self.btn_close.setText(QCoreApplication.translate("ExportReportPopup", u"Close", None))
        self.btn_excel.setText(QCoreApplication.translate("ExportReportPopup", u"Excel", None))
    # retranslateUi
