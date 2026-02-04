from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtWidgets import (QComboBox, QFrame, QHBoxLayout,
                               QLabel, QScrollArea, QSizePolicy, QSpacerItem,
                               QStackedWidget, QVBoxLayout, QWidget)


class Ui_student_test_results(object):
    def setupUi(self, student_test_results):
        if not student_test_results.objectName():
            student_test_results.setObjectName(u"student_test_results")
        student_test_results.resize(790, 700)
        student_test_results.setStyleSheet(u"background-color: rgb(240, 240, 240); font-family: \"Segoe UI\";")
        self.verticalLayout = QVBoxLayout(student_test_results)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.main_stack = QStackedWidget(student_test_results)
        self.main_stack.setObjectName(u"main_stack")
        self.page_no_tests = QWidget()
        self.page_no_tests.setObjectName(u"page_no_tests")
        self.vbox_empty = QVBoxLayout(self.page_no_tests)
        self.vbox_empty.setObjectName(u"vbox_empty")
        self.label_empty = QLabel(self.page_no_tests)
        self.label_empty.setObjectName(u"label_empty")
        self.label_empty.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vbox_empty.addWidget(self.label_empty)

        self.main_stack.addWidget(self.page_no_tests)
        self.page_test_list = QWidget()
        self.page_test_list.setObjectName(u"page_test_list")
        self.vbox_list = QVBoxLayout(self.page_test_list)
        self.vbox_list.setObjectName(u"vbox_list")
        self.vbox_list.setContentsMargins(0, 0, 0, 0)
        self.hbox_filter = QHBoxLayout()
        self.hbox_filter.setObjectName(u"hbox_filter")
        self.classes_drpdown = QComboBox(self.page_test_list)
        self.classes_drpdown.setObjectName(u"classes_drpdown")
        self.classes_drpdown.setMinimumSize(QSize(150, 35))
        self.classes_drpdown.setStyleSheet(u"QComboBox {\n"
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

        self.hbox_filter.addWidget(self.classes_drpdown)

        self.hs_filter = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hbox_filter.addItem(self.hs_filter)

        self.vbox_list.addLayout(self.hbox_filter)

        self.frame_header = QFrame(self.page_test_list)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setMinimumSize(QSize(0, 45))
        self.frame_header.setStyleSheet(u"\n"
                                        "QLabel { border: none; font-weight: 600; color: #555; font-size: 13px; }")
        self.hbox_header = QHBoxLayout(self.frame_header)
        self.hbox_header.setSpacing(10)
        self.hbox_header.setObjectName(u"hbox_header")
        self.hbox_header.setContentsMargins(20, -1, 20, -1)
        self.h_name = QLabel(self.frame_header)
        self.h_name.setObjectName(u"h_name")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.h_name.sizePolicy().hasHeightForWidth())
        self.h_name.setSizePolicy(sizePolicy)
        self.h_name.setMinimumSize(QSize(200, 0))

        self.hbox_header.addWidget(self.h_name)

        self.h_date = QLabel(self.frame_header)
        self.h_date.setObjectName(u"h_date")
        self.h_date.setMinimumSize(QSize(120, 0))

        self.hbox_header.addWidget(self.h_date)

        self.h_max = QLabel(self.frame_header)
        self.h_max.setObjectName(u"h_max")
        self.h_max.setMinimumSize(QSize(80, 0))
        self.h_max.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hbox_header.addWidget(self.h_max)

        self.h_pass = QLabel(self.frame_header)
        self.h_pass.setObjectName(u"h_pass")
        self.h_pass.setMinimumSize(QSize(80, 0))
        self.h_pass.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hbox_header.addWidget(self.h_pass)

        self.h_obt = QLabel(self.frame_header)
        self.h_obt.setObjectName(u"h_obt")
        self.h_obt.setMinimumSize(QSize(80, 0))
        self.h_obt.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hbox_header.addWidget(self.h_obt)

        self.h_status = QLabel(self.frame_header)
        self.h_status.setObjectName(u"h_status")
        self.h_status.setMinimumSize(QSize(80, 0))
        self.h_status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hbox_header.addWidget(self.h_status)

        self.vbox_list.addWidget(self.frame_header)

        self.scrollArea = QScrollArea(self.page_test_list)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(740, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollContent = QWidget()
        self.scrollContent.setObjectName(u"scrollContent")
        self.scrollContent.setGeometry(QRect(0, 0, 740, 546))
        self.container_tests = QVBoxLayout(self.scrollContent)
        self.container_tests.setSpacing(0)
        self.container_tests.setObjectName(u"container_tests")
        self.container_tests.setContentsMargins(0, 0, 0, -1)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.container_tests.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollContent)

        self.vbox_list.addWidget(self.scrollArea)

        self.main_stack.addWidget(self.page_test_list)

        self.verticalLayout.addWidget(self.main_stack)

        self.retranslateUi(student_test_results)

        self.main_stack.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(student_test_results)

    # setupUi

    def retranslateUi(self, student_test_results):
        self.main_stack.setStyleSheet(
            QCoreApplication.translate("student_test_results", u"background:transparent;", None))
        self.label_empty.setStyleSheet(
            QCoreApplication.translate("student_test_results", u"font-size: 18px; color: #999;", None))
        self.label_empty.setText(
            QCoreApplication.translate("student_test_results", u"No test results available yet.", None))
        self.classes_drpdown.setPlaceholderText(
            QCoreApplication.translate("student_test_results", u"Select class", None))
        self.h_name.setText(QCoreApplication.translate("student_test_results", u"Test Name", None))
        self.h_date.setText(QCoreApplication.translate("student_test_results", u"Date", None))
        self.h_max.setText(QCoreApplication.translate("student_test_results", u"Max Marks", None))
        self.h_pass.setText(QCoreApplication.translate("student_test_results", u"Pass Marks", None))
        self.h_obt.setText(QCoreApplication.translate("student_test_results", u"Obtained", None))
        self.h_status.setText(QCoreApplication.translate("student_test_results", u"Status", None))
        self.scrollArea.setStyleSheet(QCoreApplication.translate("student_test_results",
                                                                 u"QScrollArea { border: none; background: transparent; } QWidget { background: transparent; }",
                                                                 None))
        pass
    # retranslateUi
