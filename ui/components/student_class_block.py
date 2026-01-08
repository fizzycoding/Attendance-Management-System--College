# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'studentClass.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QProgressBar,
    QPushButton, QSizePolicy, QWidget)

class Ui_student_block(object):
    def setupUi(self, student_block):
        if not student_block.objectName():
            student_block.setObjectName(u"student_block")
        student_block.resize(950, 48)
        student_block.setMinimumSize(QSize(0, 40))
        student_block.setMaximumSize(QSize(16777215, 55))
        student_block.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        student_block.setStyleSheet(u"QProgressBar {\n"
"    border-radius: 4px;\n"
"	background-color: rgb(208, 208, 208);\n"
"	text-align: center;\n"
"	color: transparent\n"
"}\n"
"QProgressBar::chunk {\n"
"    border-radius:4px;\n"
"    background-color: rgb(42, 183, 157);   }\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"#student_block{\n"
"	border-top: 1px solid rgb(166, 166, 166);\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(student_block)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 5, 20, 5)
        self.serial_number = QLabel(student_block)
        self.serial_number.setObjectName(u"serial_number")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serial_number.sizePolicy().hasHeightForWidth())
        self.serial_number.setSizePolicy(sizePolicy)
        self.serial_number.setMinimumSize(QSize(70, 0))
        self.serial_number.setMaximumSize(QSize(60, 16777215))
        self.serial_number.setStyleSheet(u"\n"
"color: rgb(47, 47, 47);\n"
"font: 600 12pt \"Segoe UI\";")
        self.serial_number.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.serial_number)

        self.name = QPushButton(student_block)
        self.name.setObjectName(u"name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy1)
        self.name.setStyleSheet(u"color: rgb(15, 15, 15);\n"
"font: 600 12pt \"Segoe UI\";\n"
"text-align: left;\n"
"padding: 0px;\n"
"border: none")

        self.horizontalLayout.addWidget(self.name)

        self.widget_2 = QWidget(student_block)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.widget_2.setMinimumSize(QSize(0, 5))
        self.widget_2.setMaximumSize(QSize(400, 16777215))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.progressBar_attendance_rate = QProgressBar(self.widget_2)
        self.progressBar_attendance_rate.setObjectName(u"progressBar_attendance_rate")
        sizePolicy1.setHeightForWidth(self.progressBar_attendance_rate.sizePolicy().hasHeightForWidth())
        self.progressBar_attendance_rate.setSizePolicy(sizePolicy1)
        self.progressBar_attendance_rate.setMinimumSize(QSize(0, 0))
        self.progressBar_attendance_rate.setMaximumSize(QSize(300, 8))
        self.progressBar_attendance_rate.setStyleSheet(u"")
        self.progressBar_attendance_rate.setValue(50)

        self.horizontalLayout_3.addWidget(self.progressBar_attendance_rate)

        self.attendance_rate_label = QLabel(self.widget_2)
        self.attendance_rate_label.setObjectName(u"attendance_rate_label")
        sizePolicy.setHeightForWidth(self.attendance_rate_label.sizePolicy().hasHeightForWidth())
        self.attendance_rate_label.setSizePolicy(sizePolicy)
        self.attendance_rate_label.setMaximumSize(QSize(60, 16777215))
        self.attendance_rate_label.setStyleSheet(u"font: 600 12pt \"Segoe UI\";\n"
"color: rgb(36, 36, 36);")

        self.horizontalLayout_3.addWidget(self.attendance_rate_label)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(student_block)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy2)
        self.widget_3.setMaximumSize(QSize(180, 16777215))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setSpacing(30)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        sizePolicy2.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy2)
        self.widget.setMaximumSize(QSize(100, 30))
        self.widget.setStyleSheet(u"QPushButton{\n"
"	border: none\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_status = QPushButton(self.widget)
        self.btn_status.setObjectName(u"btn_status")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(20)
        sizePolicy3.setVerticalStretch(20)
        sizePolicy3.setHeightForWidth(self.btn_status.sizePolicy().hasHeightForWidth())
        self.btn_status.setSizePolicy(sizePolicy3)
        self.btn_status.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_status.setStyleSheet(u"QPushButton{\n"
"border-radius: 6px;\n"
"font: 700 10pt \"Segoe UI\";\n"
"background-color: rgba(93, 93, 93, 50);\n"
"color: rgb(93, 93, 93)\n"
"}\n"
"#status_present{\n"
"background-color: rgba(33, 195, 15, 50);\n"
"color: rgb(33, 195, 15);\n"
"}\n"
"\n"
"#status_absent{\n"
"background-color: rgba(255, 47, 28, 50);\n"
"color: rgb(255, 47, 28)\n"
"}\n"
"\n"
"#status_not_marked{\n"
"background-color: rgba(93, 93, 93, 50);\n"
"color: rgb(93, 93, 93)\n"
"}")
        self.btn_status.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btn_status)


        self.horizontalLayout_4.addWidget(self.widget)

        self.btn_remove_student = QPushButton(self.widget_3)
        self.btn_remove_student.setObjectName(u"btn_remove_student")
        sizePolicy.setHeightForWidth(self.btn_remove_student.sizePolicy().hasHeightForWidth())
        self.btn_remove_student.setSizePolicy(sizePolicy)
        self.btn_remove_student.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_remove_student.setStyleSheet(u"border: none")
        icon = QIcon()
        icon.addFile(u"icons/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_remove_student.setIcon(icon)
        self.btn_remove_student.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.btn_remove_student)


        self.horizontalLayout.addWidget(self.widget_3)


        self.retranslateUi(student_block)

        QMetaObject.connectSlotsByName(student_block)
    # setupUi

    def retranslateUi(self, student_block):
        student_block.setWindowTitle(QCoreApplication.translate("student_block", u"Form", None))
        self.serial_number.setText(QCoreApplication.translate("student_block", u"001", None))
        self.name.setText(QCoreApplication.translate("student_block", u"Sanju Patel", None))
        self.attendance_rate_label.setText(QCoreApplication.translate("student_block", u"100%", None))
        self.btn_status.setText(QCoreApplication.translate("student_block", u"Not Marked", None))
        self.btn_remove_student.setText("")
    # retranslateUi

