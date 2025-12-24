# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'attendance.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_attendance_page(object):
    def setupUi(self, attendance_page):
        if not attendance_page.objectName():
            attendance_page.setObjectName(u"attendance_page")
        attendance_page.resize(842, 562)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(attendance_page.sizePolicy().hasHeightForWidth())
        attendance_page.setSizePolicy(sizePolicy)
        attendance_page.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.verticalLayout = QVBoxLayout(attendance_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(attendance_page)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.dropdown_classes = QComboBox(self.widget)
        self.dropdown_classes.setObjectName(u"dropdown_classes")
        self.dropdown_classes.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/arrow_down.png); \n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 30px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: #ccc;\n"
"    border-left-style: solid; \n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    background: #f0f0f0; \n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white;\n"
"    border: 1px solid #ccc;\n"
"    selection-color: #159079;\n"
"    outline: 0;\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_2.addWidget(self.dropdown_classes)

        self.horizontalSpacer = QSpacerItem(587, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(30, 30, 30);\n"
"font: 600 11pt \"Segoe UI\";\n"
"")

        self.horizontalLayout_2.addWidget(self.label)

        self.invteCode_box = QPushButton(self.widget)
        self.invteCode_box.setObjectName(u"invteCode_box")
        self.invteCode_box.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.invteCode_box.setStyleSheet(u"color: #fff;\n"
"background : qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(42, 183, 157), stop:1 #067d68);;\n"
"border: none;\n"
"padding: 5px 10px;\n"
"font: 700 16px \"Segoe UI\";\n"
"border-radius: 5px")
        self.invteCode_box.setIconSize(QSize(15, 15))

        self.horizontalLayout_2.addWidget(self.invteCode_box)


        self.verticalLayout.addWidget(self.widget)

        self.students_stacked = QStackedWidget(attendance_page)
        self.students_stacked.setObjectName(u"students_stacked")
        self.no_student = QWidget()
        self.no_student.setObjectName(u"no_student")
        self.verticalLayout_5 = QVBoxLayout(self.no_student)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_2 = QWidget(self.no_student)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QLabel{\n"
"  \n"
"  font: 15pt \"Segoe UI\";\n"
"  color: rgb(0, 0, 0);\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)


        self.verticalLayout_5.addWidget(self.widget_2)

        self.students_stacked.addWidget(self.no_student)
        self.all_student = QWidget()
        self.all_student.setObjectName(u"all_student")
        self.verticalLayout_3 = QVBoxLayout(self.all_student)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.students_list_container = QScrollArea(self.all_student)
        self.students_list_container.setObjectName(u"students_list_container")
        self.students_list_container.setWidgetResizable(True)
        self.students_list_container.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 820, 483))
        self.classesLayout = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.classesLayout.setObjectName(u"classesLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.classesLayout.addItem(self.verticalSpacer)

        self.students_list_container.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_3.addWidget(self.students_list_container)

        self.students_stacked.addWidget(self.all_student)

        self.verticalLayout.addWidget(self.students_stacked)


        self.retranslateUi(attendance_page)

        self.students_stacked.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(attendance_page)
    # setupUi

    def retranslateUi(self, attendance_page):
        attendance_page.setWindowTitle(QCoreApplication.translate("attendance_page", u"Form", None))
        self.label.setText(QCoreApplication.translate("attendance_page", u"Invite Code: ", None))
        self.invteCode_box.setText(QCoreApplication.translate("attendance_page", u"AWJDK", None))
        self.label_2.setText(QCoreApplication.translate("attendance_page", u"No students, Invite some!", None))
    # retranslateUi

