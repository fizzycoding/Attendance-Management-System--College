# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testResultStudentRow.ui'
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
    QSizePolicy, QWidget)

class Ui_student_test_card(object):
    def setupUi(self, student_test_card):
        if not student_test_card.objectName():
            student_test_card.setObjectName(u"student_test_card")
        student_test_card.resize(950, 50)
        student_test_card.setMinimumSize(QSize(0, 50))
        student_test_card.setMaximumSize(QSize(16777215, 60))
        student_test_card.setStyleSheet(u"#student_test_card {\n"
"                background-color: white;\n"
"                border-bottom: 1px solid #e0e0e0;\n"
"                border-left: 1px solid #ddd;\n"
"                border-right: 1px solid #ddd;\n"
"                border-radius: 0px;\n"
"                }\n"
"                #student_test_card:hover {\n"
"                background-color: #fcfcfc;\n"
"                }\n"
"                QLabel { border: none; background: transparent; }\n"
"            ")
        self.horizontalLayout = QHBoxLayout(student_test_card)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 0, 20, 0)
        self.lbl_name = QLabel(student_test_card)
        self.lbl_name.setObjectName(u"lbl_name")
        self.lbl_name.setMinimumSize(QSize(200, 0))
        self.lbl_name.setStyleSheet(u"font: 600 11pt \"Segoe UI\"; color: #333;")
        self.lbl_name.setWordWrap(True)

        self.horizontalLayout.addWidget(self.lbl_name)

        self.lbl_date = QLabel(student_test_card)
        self.lbl_date.setObjectName(u"lbl_date")
        self.lbl_date.setMinimumSize(QSize(120, 0))
        self.lbl_date.setStyleSheet(u"color: #444; \n"
"font: 600 10pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.lbl_date)

        self.lbl_max = QLabel(student_test_card)
        self.lbl_max.setObjectName(u"lbl_max")
        self.lbl_max.setMinimumSize(QSize(80, 0))
        self.lbl_max.setStyleSheet(u"color: #444; \n"
"font: 600 10pt \"Segoe UI\";")
        self.lbl_max.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lbl_max)

        self.lbl_pass = QLabel(student_test_card)
        self.lbl_pass.setObjectName(u"lbl_pass")
        self.lbl_pass.setMinimumSize(QSize(80, 0))
        self.lbl_pass.setStyleSheet(u"color: #444; \n"
"font: 600 10pt \"Segoe UI\";")
        self.lbl_pass.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lbl_pass)

        self.lbl_score = QLabel(student_test_card)
        self.lbl_score.setObjectName(u"lbl_score")
        self.lbl_score.setMinimumSize(QSize(80, 0))
        self.lbl_score.setStyleSheet(u"font: 700 10pt \"Segoe UI\"; color: #333;")
        self.lbl_score.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lbl_score)

        self.lbl_status = QLabel(student_test_card)
        self.lbl_status.setObjectName(u"lbl_status")
        self.lbl_status.setMinimumSize(QSize(80, 26))
        self.lbl_status.setMaximumSize(QSize(80, 26))
        self.lbl_status.setStyleSheet(u"background-color: #E0F2F1; color: #009688; border-radius: 4px; font-weight:\n"
"                            bold; font-size: 11px;\n"
"                        ")
        self.lbl_status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lbl_status)


        self.retranslateUi(student_test_card)

        QMetaObject.connectSlotsByName(student_test_card)
    # setupUi

    def retranslateUi(self, student_test_card):
        self.lbl_name.setText(QCoreApplication.translate("student_test_card", u"Test Name", None))
        self.lbl_date.setText(QCoreApplication.translate("student_test_card", u"2025-01-28", None))
        self.lbl_max.setText(QCoreApplication.translate("student_test_card", u"50", None))
        self.lbl_pass.setText(QCoreApplication.translate("student_test_card", u"17", None))
        self.lbl_score.setText(QCoreApplication.translate("student_test_card", u"42", None))
        self.lbl_status.setText(QCoreApplication.translate("student_test_card", u"PASS", None))
        pass
    # retranslateUi

