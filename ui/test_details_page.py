from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QCursor,
                           QIcon)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel,
                               QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget)


class Ui_test_details_page(object):
    def setupUi(self, test_details_page):
        if not test_details_page.objectName():
            test_details_page.setObjectName(u"test_details_page")
        test_details_page.resize(842, 562)
        test_details_page.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.verticalLayout = QVBoxLayout(test_details_page)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(18, -1, 18, -1)
        self.header_widget = QWidget(test_details_page)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setStyleSheet(u"background-color: transparent;")
        self.horizontalLayout_header = QHBoxLayout(self.header_widget)
        self.horizontalLayout_header.setObjectName(u"horizontalLayout_header")
        self.horizontalLayout_header.setContentsMargins(0, 0, 0, 0)
        self.btn_back = QPushButton(self.header_widget)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_back.setStyleSheet(u"\n"
                                    "          QPushButton {\n"
                                    "           border: none;\n"
                                    "           border-radius: 20px;\n"
                                    "           padding: 5px;\n"
                                    "          }\n"
                                    "          QPushButton:hover {\n"
                                    "           background-color: #e0e0e0;\n"
                                    "          }\n"
                                    "         ")
        icon = QIcon()
        icon.addFile(u"icons/back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_back.setIcon(icon)
        self.btn_back.setIconSize(QSize(24, 24))
        self.btn_back.setProperty(u"fixedSize", QSize(40, 40))

        self.horizontalLayout_header.addWidget(self.btn_back)

        self.info_container = QWidget(self.header_widget)
        self.info_container.setObjectName(u"info_container")
        self.verticalLayout_info = QVBoxLayout(self.info_container)
        self.verticalLayout_info.setSpacing(2)
        self.verticalLayout_info.setObjectName(u"verticalLayout_info")
        self.verticalLayout_info.setContentsMargins(10, -1, -1, -1)
        self.label_test_name = QLabel(self.info_container)
        self.label_test_name.setObjectName(u"label_test_name")
        self.label_test_name.setStyleSheet(u"font: 700 16pt \"Segoe UI\"; color: #333;")

        self.verticalLayout_info.addWidget(self.label_test_name)

        self.details_row = QWidget(self.info_container)
        self.details_row.setObjectName(u"details_row")
        self.horizontalLayout_details = QHBoxLayout(self.details_row)
        self.horizontalLayout_details.setSpacing(15)
        self.horizontalLayout_details.setObjectName(u"horizontalLayout_details")
        self.horizontalLayout_details.setContentsMargins(0, 0, -1, 0)
        self.label_max = QLabel(self.details_row)
        self.label_max.setObjectName(u"label_max")
        self.label_max.setStyleSheet(u"font: 10pt \"Segoe UI\"; color: #666;")

        self.horizontalLayout_details.addWidget(self.label_max)

        self.label_pass = QLabel(self.details_row)
        self.label_pass.setObjectName(u"label_pass")
        self.label_pass.setStyleSheet(u"font: 10pt \"Segoe UI\"; color: #666;")

        self.horizontalLayout_details.addWidget(self.label_pass)

        self.label_date = QLabel(self.details_row)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setStyleSheet(u"font: 10pt \"Segoe UI\"; color: #666;")

        self.horizontalLayout_details.addWidget(self.label_date)

        self.horizontalSpacer_details = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_details.addItem(self.horizontalSpacer_details)

        self.verticalLayout_info.addWidget(self.details_row)

        self.horizontalLayout_header.addWidget(self.info_container)

        self.horizontalSpacer_main = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_header.addItem(self.horizontalSpacer_main)

        self.btn_save_marks = QPushButton(self.header_widget)
        self.btn_save_marks.setObjectName(u"btn_save_marks")
        self.btn_save_marks.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_save_marks.setStyleSheet(u"\n"
                                          "color: #fff;\n"
                                          "background : #3388FF;\n"
                                          "border: none;\n"
                                          "padding: 10px 20px;\n"
                                          "font: 600 14px \"Segoe UI\";\n"
                                          "border-radius: 7px")
        icon1 = QIcon()
        icon1.addFile(u"icons/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_save_marks.setIcon(icon1)

        self.horizontalLayout_header.addWidget(self.btn_save_marks)

        self.verticalLayout.addWidget(self.header_widget)

        self.container = QWidget(test_details_page)
        self.container.setObjectName(u"container")
        self.container.setStyleSheet(u"#container{background-color: rgb(255, 255, 255);\n"
                                     "border:1px solid rgb(187, 187, 187); border-radius: 10px}")
        self.verticalLayout_2 = QVBoxLayout(self.container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 5, 3, 5)
        self.tableHeader = QFrame(self.container)
        self.tableHeader.setObjectName(u"tableHeader")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableHeader.sizePolicy().hasHeightForWidth())
        self.tableHeader.setSizePolicy(sizePolicy)
        self.tableHeader.setMinimumSize(QSize(0, 0))
        self.tableHeader.setStyleSheet(u"QFrame{boder:none; background-color:transparent;}\n"
                                       "\n"
                                       "QLabel {\n"
                                       "    font-size: 12px;\n"
                                       "    color: #555;\n"
                                       "    font-weight: 600;\n"
                                       "border: none\n"
                                       "\n"
                                       "}\n"
                                       "          ")
        self.headerRowLayout = QHBoxLayout(self.tableHeader)
        self.headerRowLayout.setObjectName(u"headerRowLayout")
        self.headerRowLayout.setContentsMargins(17, 12, 17, 12)
        self.label = QLabel(self.tableHeader)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(50, 0))

        self.headerRowLayout.addWidget(self.label)

        self.head_student = QLabel(self.tableHeader)
        self.head_student.setObjectName(u"head_student")
        self.head_student.setMinimumSize(QSize(220, 0))

        self.headerRowLayout.addWidget(self.head_student)

        self.head_status = QLabel(self.tableHeader)
        self.head_status.setObjectName(u"head_status")
        sizePolicy1.setHeightForWidth(self.head_status.sizePolicy().hasHeightForWidth())
        self.head_status.setSizePolicy(sizePolicy1)
        self.head_status.setMinimumSize(QSize(100, 0))
        self.head_status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.headerRowLayout.addWidget(self.head_status)

        self.head_action = QLabel(self.tableHeader)
        self.head_action.setObjectName(u"head_action")
        sizePolicy1.setHeightForWidth(self.head_action.sizePolicy().hasHeightForWidth())
        self.head_action.setSizePolicy(sizePolicy1)
        self.head_action.setMinimumSize(QSize(100, 0))
        self.head_action.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTrailing | Qt.AlignmentFlag.AlignVCenter)

        self.headerRowLayout.addWidget(self.head_action)

        self.verticalLayout_2.addWidget(self.tableHeader)

        self.scrollArea = QScrollArea(self.container)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color: transparent;\n"
                                      "")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.widget_2 = QWidget()
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 800, 418))
        self.widget_2.setStyleSheet(u"")
        self.studentsLayout = QVBoxLayout(self.widget_2)
        self.studentsLayout.setSpacing(0)
        self.studentsLayout.setObjectName(u"studentsLayout")
        self.studentsLayout.setContentsMargins(0, 0, 0, -1)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.studentsLayout.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.widget_2)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.verticalLayout.addWidget(self.container)

        self.retranslateUi(test_details_page)

        QMetaObject.connectSlotsByName(test_details_page)

    # setupUi

    def retranslateUi(self, test_details_page):
        test_details_page.setWindowTitle(QCoreApplication.translate("test_details_page", u"Test Details", None))
        self.btn_back.setText("")
        self.label_test_name.setText(QCoreApplication.translate("test_details_page", u"Unit Test 1", None))
        self.label_max.setText(QCoreApplication.translate("test_details_page", u"Max Marks: 50", None))
        self.label_pass.setText(QCoreApplication.translate("test_details_page", u"Min Marks: 17", None))
        self.label_date.setText(QCoreApplication.translate("test_details_page", u"Date: 28-Dec-2025", None))
        self.btn_save_marks.setText(QCoreApplication.translate("test_details_page", u"Save Marks", None))
        self.label.setText(QCoreApplication.translate("test_details_page", u"S.No.", None))
        self.head_student.setText(QCoreApplication.translate("test_details_page", u"Name", None))
        self.head_status.setText(QCoreApplication.translate("test_details_page", u"Marks", None))
        self.head_action.setText(QCoreApplication.translate("test_details_page", u"Result", None))
    # retranslateUi
