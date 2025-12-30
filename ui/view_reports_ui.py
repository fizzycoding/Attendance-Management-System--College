# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewReports.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_view_reports_page(object):
    def setupUi(self, view_reports_page):
        if not view_reports_page.objectName():
            view_reports_page.setObjectName(u"view_reports_page")
        view_reports_page.resize(842, 557)
        view_reports_page.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.verticalLayout = QVBoxLayout(view_reports_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header_widget = QWidget(view_reports_page)
        self.header_widget.setObjectName(u"header_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_widget.sizePolicy().hasHeightForWidth())
        self.header_widget.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.dropdown_classes = QComboBox(self.header_widget)
        self.dropdown_classes.setObjectName(u"dropdown_classes")
        self.dropdown_classes.setEnabled(True)
        self.dropdown_classes.setMinimumSize(QSize(150, 0))
        self.dropdown_classes.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
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
"QComboBox QAbstractItemView {\n"
"    background-color: white;\n"
"    border: 1px solid #ccc;\n"
"    selection-color: #159079;\n"
"    outline: 0;\n"
"    color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_2.addWidget(self.dropdown_classes)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_new_test = QPushButton(self.header_widget)
        self.btn_new_test.setObjectName(u"btn_new_test")
        self.btn_new_test.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_new_test.setStyleSheet(u"color: #fff;\n"
"background : qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(42, 183, 157), stop:1 #067d68);;\n"
"border: none;\n"
"padding: 10px 20px;\n"
"font: 800 14px \"Segoe UI\";\n"
"border-radius: 7px")

        self.horizontalLayout_2.addWidget(self.btn_new_test)


        self.verticalLayout.addWidget(self.header_widget)

        self.content_stack = QStackedWidget(view_reports_page)
        self.content_stack.setObjectName(u"content_stack")
        self.no_classes = QWidget()
        self.no_classes.setObjectName(u"no_classes")
        self.verticalLayout_empty = QVBoxLayout(self.no_classes)
        self.verticalLayout_empty.setObjectName(u"verticalLayout_empty")
        self.label_no_test = QLabel(self.no_classes)
        self.label_no_test.setObjectName(u"label_no_test")
        self.label_no_test.setStyleSheet(u"font: 15pt \"Segoe UI\"; color: rgb(100, 100, 100);")
        self.label_no_test.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_empty.addWidget(self.label_no_test)

        self.content_stack.addWidget(self.no_classes)
        self.no_student = QWidget()
        self.no_student.setObjectName(u"no_student")
        self.no_student.setStyleSheet(u"font: 15pt \"Segoe UI\"; color: rgb(100, 100, 100);")
        self.verticalLayout_9 = QVBoxLayout(self.no_student)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_2 = QLabel(self.no_student)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 15pt \"Segoe UI\"; color: rgb(100, 100, 100);")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_2)

        self.content_stack.addWidget(self.no_student)
        self.classes_selected = QWidget()
        self.classes_selected.setObjectName(u"classes_selected")
        self.verticalLayout_list = QVBoxLayout(self.classes_selected)
        self.verticalLayout_list.setObjectName(u"verticalLayout_list")
        self.verticalLayout_list.setContentsMargins(0, 0, 0, 0)
        self.main_container = QWidget(self.classes_selected)
        self.main_container.setObjectName(u"main_container")
        self.horizontalLayout = QHBoxLayout(self.main_container)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_container = QWidget(self.main_container)
        self.left_container.setObjectName(u"left_container")
        self.verticalLayout_2 = QVBoxLayout(self.left_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.left_container)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setStyleSheet(u"QLabel{ color: #383838; font: 600 9pt \"Segoe UI\"; }")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(70, 100))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_5)


        self.verticalLayout_2.addWidget(self.frame)

        self.scrollArea = QScrollArea(self.left_container)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 464, 432))
        self.all_students_container = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.all_students_container.setSpacing(0)
        self.all_students_container.setObjectName(u"all_students_container")
        self.all_students_container.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 412, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.all_students_container.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.horizontalLayout.addWidget(self.left_container)

        self.right_container = QWidget(self.main_container)
        self.right_container.setObjectName(u"right_container")
        self.verticalLayout_3 = QVBoxLayout(self.right_container)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_7 = QLabel(self.right_container)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: #383838; font: 600 9pt \"Segoe UI\";")

        self.verticalLayout_3.addWidget(self.label_7)

        self.top_cards_container = QWidget(self.right_container)
        self.top_cards_container.setObjectName(u"top_cards_container")
        self.top_cards_container.setStyleSheet(u"#card1, #card2, #card3{\n"
"  background-color: rgb(255, 255, 255);\n"
"  border-radius: 8px;\n"
"  border:1px solid rgb(200,200,200);\n"
"}\n"
"#card1:hover ,#card2:hover ,#card3:hover {\n"
"    border: 1px solid #2ab79d;\n"
"    background-color: #fcfcfc;\n"
"}\n"
"\n"
"QPushButton{\n"
"  background-color: transparent;\n"
"  color: rgb(88, 88, 88);\n"
"  font: 600 11pt \"Segoe UI\";\n"
"  border: none\n"
"}\n"
"QLabel{\n"
"  background-color: transparent;\n"
"  color: rgb(34, 34, 34);\n"
"  font: 800 25pt \"Segoe UI\";\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.top_cards_container)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.card1 = QWidget(self.top_cards_container)
        self.card1.setObjectName(u"card1")
        self.verticalLayout_4 = QVBoxLayout(self.card1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton = QPushButton(self.card1)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u"../../icons/board.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)

        self.verticalLayout_4.addWidget(self.pushButton)

        self.classes_attended_count = QLabel(self.card1)
        self.classes_attended_count.setObjectName(u"classes_attended_count")
        self.classes_attended_count.setStyleSheet(u"color: rgb(28, 164, 255);")
        self.classes_attended_count.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.classes_attended_count)


        self.horizontalLayout_4.addWidget(self.card1)

        self.card3 = QWidget(self.top_cards_container)
        self.card3.setObjectName(u"card3")
        self.verticalLayout_5 = QVBoxLayout(self.card3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton_2 = QPushButton(self.card3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon1 = QIcon()
        icon1.addFile(u"../../icons/present.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon1)

        self.verticalLayout_5.addWidget(self.pushButton_2)

        self.present_count = QLabel(self.card3)
        self.present_count.setObjectName(u"present_count")
        self.present_count.setStyleSheet(u"color: rgb(86, 213, 86);")
        self.present_count.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.present_count)


        self.horizontalLayout_4.addWidget(self.card3)

        self.card2 = QWidget(self.top_cards_container)
        self.card2.setObjectName(u"card2")
        self.verticalLayout_6 = QVBoxLayout(self.card2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_3 = QPushButton(self.card2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon2 = QIcon()
        icon2.addFile(u"../../icons/absent.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon2)

        self.verticalLayout_6.addWidget(self.pushButton_3)

        self.absent_count = QLabel(self.card2)
        self.absent_count.setObjectName(u"absent_count")
        self.absent_count.setStyleSheet(u"color:rgb(255, 82, 52)")
        self.absent_count.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.absent_count)


        self.horizontalLayout_4.addWidget(self.card2)


        self.verticalLayout_3.addWidget(self.top_cards_container)

        self.test_conttainer = QWidget(self.right_container)
        self.test_conttainer.setObjectName(u"test_conttainer")
        self.verticalLayout_8 = QVBoxLayout(self.test_conttainer)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, -1, 0, -1)
        self.label_8 = QLabel(self.test_conttainer)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: #383838; font: 600 9pt \"Segoe UI\";")

        self.verticalLayout_8.addWidget(self.label_8)

        self.stackedWidget = QStackedWidget(self.test_conttainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.no_test_found = QWidget()
        self.no_test_found.setObjectName(u"no_test_found")
        self.verticalLayout_7 = QVBoxLayout(self.no_test_found)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.no_test_found)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: #383838; font: 600 9pt \"Segoe UI\";")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label)

        self.stackedWidget.addWidget(self.no_test_found)
        self.test_list = QWidget()
        self.test_list.setObjectName(u"test_list")
        self.verticalLayout_test_list = QVBoxLayout(self.test_list)
        self.verticalLayout_test_list.setObjectName(u"verticalLayout_test_list")
        self.verticalLayout_test_list.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_tests = QScrollArea(self.test_list)
        self.scrollArea_tests.setObjectName(u"scrollArea_tests")
        self.scrollArea_tests.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_tests.setWidgetResizable(True)
        self.scrollAreaWidgetContents_tests = QWidget()
        self.scrollAreaWidgetContents_tests.setObjectName(u"scrollAreaWidgetContents_tests")
        self.scrollAreaWidgetContents_tests.setGeometry(QRect(0, 0, 304, 282))
        self.test_results_layout = QVBoxLayout(self.scrollAreaWidgetContents_tests)
        self.test_results_layout.setSpacing(10)
        self.test_results_layout.setObjectName(u"test_results_layout")
        self.test_results_layout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.test_results_layout.addItem(self.verticalSpacer_2)

        self.scrollArea_tests.setWidget(self.scrollAreaWidgetContents_tests)

        self.verticalLayout_test_list.addWidget(self.scrollArea_tests)

        self.stackedWidget.addWidget(self.test_list)

        self.verticalLayout_8.addWidget(self.stackedWidget)


        self.verticalLayout_3.addWidget(self.test_conttainer)

        self.verticalLayout_3.setStretch(1, 2)
        self.verticalLayout_3.setStretch(2, 6)

        self.horizontalLayout.addWidget(self.right_container)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout_list.addWidget(self.main_container)

        self.content_stack.addWidget(self.classes_selected)

        self.verticalLayout.addWidget(self.content_stack)


        self.retranslateUi(view_reports_page)

        self.content_stack.setCurrentIndex(2)
        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(view_reports_page)
    # setupUi

    def retranslateUi(self, view_reports_page):
        view_reports_page.setWindowTitle(QCoreApplication.translate("view_reports_page", u"Tests Dashboard", None))
        self.btn_new_test.setText(QCoreApplication.translate("view_reports_page", u"Download", None))
        self.label_no_test.setText(QCoreApplication.translate("view_reports_page", u"Select Any Class Or Create A New class", None))
        self.label_2.setText(QCoreApplication.translate("view_reports_page", u"No Students, Invite some", None))
        self.label_3.setText(QCoreApplication.translate("view_reports_page", u"S. No.", None))
        self.label_4.setText(QCoreApplication.translate("view_reports_page", u"Name", None))
        self.label_5.setText(QCoreApplication.translate("view_reports_page", u"Attendance", None))
        self.label_7.setText(QCoreApplication.translate("view_reports_page", u"Attendance Record", None))
        self.pushButton.setText(QCoreApplication.translate("view_reports_page", u"Classes", None))
        self.classes_attended_count.setText(QCoreApplication.translate("view_reports_page", u"0", None))
        self.pushButton_2.setText(QCoreApplication.translate("view_reports_page", u"Present", None))
        self.present_count.setText(QCoreApplication.translate("view_reports_page", u"0", None))
        self.pushButton_3.setText(QCoreApplication.translate("view_reports_page", u"Absent", None))
        self.absent_count.setText(QCoreApplication.translate("view_reports_page", u"0", None))
        self.label_8.setText(QCoreApplication.translate("view_reports_page", u"Recent test results", None))
        self.label.setText(QCoreApplication.translate("view_reports_page", u"No Test Found", None))
    # retranslateUi

