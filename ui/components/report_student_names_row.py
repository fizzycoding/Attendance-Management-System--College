# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reportStudentNamesRow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_reportStudentNameRow(object):
    def setupUi(self, reportStudentNameRow):
        if not reportStudentNameRow.objectName():
            reportStudentNameRow.setObjectName(u"reportStudentNameRow")
        reportStudentNameRow.resize(569, 45)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(reportStudentNameRow.sizePolicy().hasHeightForWidth())
        reportStudentNameRow.setSizePolicy(sizePolicy)
        reportStudentNameRow.setMinimumSize(QSize(0, 45))
        reportStudentNameRow.setMaximumSize(QSize(16777215, 45))
        reportStudentNameRow.setStyleSheet(u"#reportStudentNameRow{border-top: 1px solid;\n"
"border-top-color: rgb(200,200,200);}\n"
"#reportStudentNameRow:hover{\n"
"background-color: rgb(231, 255, 243)}\n"
"QLabel{background-color:transparent}")
        self.horizontalLayout = QHBoxLayout(reportStudentNameRow)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, 0, 0, 0)
        self.sNumber = QLabel(reportStudentNameRow)
        self.sNumber.setObjectName(u"sNumber")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(55)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sNumber.sizePolicy().hasHeightForWidth())
        self.sNumber.setSizePolicy(sizePolicy1)
        self.sNumber.setMinimumSize(QSize(60, 0))
        self.sNumber.setStyleSheet(u"color: #383838; font: 600 9pt \"Segoe UI\";")
        self.sNumber.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.sNumber)

        self.name = QLabel(reportStudentNameRow)
        self.name.setObjectName(u"name")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy2)
        self.name.setStyleSheet(u"color: rgb(43, 43, 43); font: 600 10pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.name)

        self.rate = QLabel(reportStudentNameRow)
        self.rate.setObjectName(u"rate")
        sizePolicy2.setHeightForWidth(self.rate.sizePolicy().hasHeightForWidth())
        self.rate.setSizePolicy(sizePolicy2)
        self.rate.setMaximumSize(QSize(70, 16777215))
        self.rate.setStyleSheet(u"color: rgb(28, 164, 255);\n"
"font: 700 10pt \"Segoe UI\";")
        self.rate.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.rate)


        self.retranslateUi(reportStudentNameRow)

        QMetaObject.connectSlotsByName(reportStudentNameRow)
    # setupUi

    def retranslateUi(self, reportStudentNameRow):
        reportStudentNameRow.setWindowTitle(QCoreApplication.translate("reportStudentNameRow", u"Form", None))
        self.sNumber.setText(QCoreApplication.translate("reportStudentNameRow", u"1", None))
        self.name.setText(QCoreApplication.translate("reportStudentNameRow", u"Rahul", None))
        self.rate.setText(QCoreApplication.translate("reportStudentNameRow", u"90%", None))
    # retranslateUi

