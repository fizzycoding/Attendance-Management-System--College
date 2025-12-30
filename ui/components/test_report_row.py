# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testReportRow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_test_report_row(object):
    def setupUi(self, test_report_row):
        if not test_report_row.objectName():
            test_report_row.setObjectName(u"test_report_row")
        test_report_row.resize(380, 85)
        test_report_row.setMinimumSize(QSize(0, 85))
        test_report_row.setMaximumSize(QSize(16777215, 90))
        test_report_row.setStyleSheet(u"QFrame#test_report_row {\n"
"    background-color: white;\n"
"    border-radius: 12px;\n"
"    border: 1px solid #e0e0e0;\n"
"}\n"
"QFrame#test_report_row:hover {\n"
"    border: 1px solid #2ab79d;\n"
"    background-color: #fcfcfc;\n"
"}\n"
"QLabel {\n"
"    border: none;\n"
"    background: transparent;\n"
"}")
        self.horizontalLayout = QHBoxLayout(test_report_row)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 10, 20, 10)
        self.verticalLayout_info = QVBoxLayout()
        self.verticalLayout_info.setSpacing(5)
        self.verticalLayout_info.setObjectName(u"verticalLayout_info")
        self.test_name = QLabel(test_report_row)
        self.test_name.setObjectName(u"test_name")
        self.test_name.setStyleSheet(u"font: 700 13pt \"Segoe UI\"; color: #222;")

        self.verticalLayout_info.addWidget(self.test_name)

        self.horizontalLayout_stats = QHBoxLayout()
        self.horizontalLayout_stats.setSpacing(15)
        self.horizontalLayout_stats.setObjectName(u"horizontalLayout_stats")
        self.marks_label = QLabel(test_report_row)
        self.marks_label.setObjectName(u"marks_label")
        self.marks_label.setStyleSheet(u"color: #2ab79d; font-weight: 800; font-family: \"Segoe UI\"; font-size: 11pt;")

        self.horizontalLayout_stats.addWidget(self.marks_label)

        self.passing_label = QLabel(test_report_row)
        self.passing_label.setObjectName(u"passing_label")
        self.passing_label.setStyleSheet(u"color: #888; font-family: \"Segoe UI\"; font-size: 10pt; font-weight: 500;")

        self.horizontalLayout_stats.addWidget(self.passing_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_stats.addItem(self.horizontalSpacer)


        self.verticalLayout_info.addLayout(self.horizontalLayout_stats)


        self.horizontalLayout.addLayout(self.verticalLayout_info)

        self.chart_container = QFrame(test_report_row)
        self.chart_container.setObjectName(u"chart_container")
        self.chart_container.setMinimumSize(QSize(60, 60))
        self.chart_container.setMaximumSize(QSize(60, 60))
        self.chart_container.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout.addWidget(self.chart_container)


        self.retranslateUi(test_report_row)

        QMetaObject.connectSlotsByName(test_report_row)
    # setupUi

    def retranslateUi(self, test_report_row):
        self.test_name.setText(QCoreApplication.translate("test_report_row", u"Unit Test 1", None))
        self.marks_label.setText(QCoreApplication.translate("test_report_row", u"45/50", None))
        self.passing_label.setText(QCoreApplication.translate("test_report_row", u"Min: 17", None))
        pass
    # retranslateUi

