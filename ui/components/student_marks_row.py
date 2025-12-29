# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'studentMarksRow.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QWidget)

class Ui_student_marks_row(object):
    def setupUi(self, student_marks_row):
        if not student_marks_row.objectName():
            student_marks_row.setObjectName(u"student_marks_row")
        student_marks_row.resize(750, 48)
        student_marks_row.setMinimumSize(QSize(0, 48))
        student_marks_row.setMaximumSize(QSize(16777215, 55))
        student_marks_row.setStyleSheet(u"\n"
"    QFrame#student_marks_row {\n"
"        border-top: 1px solid ;\n"
"	border-color: rgb(124, 124, 124);\n"
"        border-bottom: none;\n"
"    }\n"
"   QLabel{\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout = QHBoxLayout(student_marks_row)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, 5, 15, 5)
        self.serial_no = QLabel(student_marks_row)
        self.serial_no.setObjectName(u"serial_no")
        self.serial_no.setStyleSheet(u"color: #777; font-size: 14px;")
        self.serial_no.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.serial_no.setProperty(u"fixedSize", QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.serial_no)

        self.student_name = QLabel(student_marks_row)
        self.student_name.setObjectName(u"student_name")
        self.student_name.setStyleSheet(u"font-weight: 600; font-size: 12pt; font-family: \"Segoe UI\"; color: #333;")

        self.horizontalLayout.addWidget(self.student_name)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_marks = QLabel(student_marks_row)
        self.label_marks.setObjectName(u"label_marks")
        self.label_marks.setStyleSheet(u"color: #999; font-size: 13px; margin-right: 5px;")

        self.horizontalLayout.addWidget(self.label_marks)

        self.input_marks = QSpinBox(student_marks_row)
        self.input_marks.setObjectName(u"input_marks")
        self.input_marks.setStyleSheet(u"\n"
"       QSpinBox {\n"
"        border: none; \n"
"        color: #333;\n"
"        border-radius: 4px; \n"
"        padding: 0px; \n"
"        background: transparent;\n"
"        font-size: 14px;\n"
"        font-weight: bold;\n"
"       }\n"
"       QSpinBox:focus, QSpinBox:hover {\n"
"        border: 1px solid #2ab79d;\n"
"        background: white;\n"
"       }\n"
"      ")
        self.input_marks.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_marks.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.input_marks.setMaximum(1000)
        self.input_marks.setProperty(u"fixedSize", QSize(45, 25))

        self.horizontalLayout.addWidget(self.input_marks)

        self.btn_status = QPushButton(student_marks_row)
        self.btn_status.setObjectName(u"btn_status")
        self.btn_status.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_status.sizePolicy().hasHeightForWidth())
        self.btn_status.setSizePolicy(sizePolicy)
        self.btn_status.setMinimumSize(QSize(100, 0))
        self.btn_status.setStyleSheet(u"       QPushButton {\n"
"        border: none;\n"
"        border-radius: 4px;\n"
"        padding: 4px 8px;\n"
"        font-weight: bold;\n"
"        font-size: 11px;\n"
"        background-color: ; \n"
"	color: rgb(181, 181, 181);\n"
"        color: #9E9E9E;\n"
"       }\n"
"\n"
"	#pass{\n"
"                background-color: rgb(184, 242, 210); \n"
"                color: #009688; \n"
"}\n"
"\n"
"#fail{\n"
"	 background-color: rgb(255, 202, 210); \n"
"                color: #D32F2F; \n"
"}\n"
"      ")
        self.btn_status.setProperty(u"fixedSize", QSize(110, 28))

        self.horizontalLayout.addWidget(self.btn_status)


        self.retranslateUi(student_marks_row)

        QMetaObject.connectSlotsByName(student_marks_row)
    # setupUi

    def retranslateUi(self, student_marks_row):
        self.serial_no.setText(QCoreApplication.translate("student_marks_row", u"1", None))
        self.student_name.setText(QCoreApplication.translate("student_marks_row", u"Student Name", None))
        self.label_marks.setText(QCoreApplication.translate("student_marks_row", u"Marks:", None))
        self.btn_status.setText(QCoreApplication.translate("student_marks_row", u"Not Attempted", None))
        pass
    # retranslateUi

