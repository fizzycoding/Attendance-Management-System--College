from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QCursor,
                           QIcon)
from PySide6.QtWidgets import (QComboBox, QFrame, QHBoxLayout,
                               QLabel, QPushButton, QScrollArea, QSizePolicy,
                               QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)


class Ui_attendance_page(object):
    def setupUi(self, attendance_page):
        if not attendance_page.objectName():
            attendance_page.setObjectName(u"attendance_page")
        attendance_page.resize(842, 551)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(attendance_page.sizePolicy().hasHeightForWidth())
        attendance_page.setSizePolicy(sizePolicy)
        attendance_page.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.verticalLayout = QVBoxLayout(attendance_page)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(18, -1, 18, -1)
        self.widget = QWidget(attendance_page)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setStyleSheet(u"background-color: transparent;\n"
                                  "border:none")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, 9)
        self.dropdown_classes = QComboBox(self.widget)
        self.dropdown_classes.setObjectName(u"dropdown_classes")
        self.dropdown_classes.setMinimumSize(QSize(200, 40))
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

        self.horizontalSpacer_Left = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_Left)

        self.date_control_container = QWidget(self.widget)
        self.date_control_container.setObjectName(u"date_control_container")
        self.date_control_container.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.date_control_container)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_prev_date = QPushButton(self.date_control_container)
        self.btn_prev_date.setObjectName(u"btn_prev_date")
        self.btn_prev_date.setMinimumSize(QSize(15, 15))
        self.btn_prev_date.setMaximumSize(QSize(15, 15))
        self.btn_prev_date.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"icons/prev.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_prev_date.setIcon(icon)
        self.btn_prev_date.setIconSize(QSize(12, 12))
        self.btn_prev_date.setProperty(u"fixedSize", QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.btn_prev_date)

        self.btn_date_picker = QPushButton(self.date_control_container)
        self.btn_date_picker.setObjectName(u"btn_date_picker")
        sizePolicy.setHeightForWidth(self.btn_date_picker.sizePolicy().hasHeightForWidth())
        self.btn_date_picker.setSizePolicy(sizePolicy)
        self.btn_date_picker.setMinimumSize(QSize(10, 10))
        self.btn_date_picker.setMaximumSize(QSize(48544, 54545))
        self.btn_date_picker.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_date_picker.setStyleSheet(u"font: 600 12pt \"Segoe UI\";\n"
                                           "color: rgb(0, 0, 0);")

        self.horizontalLayout_3.addWidget(self.btn_date_picker)

        self.btn_next_date = QPushButton(self.date_control_container)
        self.btn_next_date.setObjectName(u"btn_next_date")
        self.btn_next_date.setMinimumSize(QSize(15, 15))
        self.btn_next_date.setMaximumSize(QSize(15, 15))
        self.btn_next_date.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"icons/next.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_next_date.setIcon(icon1)
        self.btn_next_date.setIconSize(QSize(12, 12))
        self.btn_next_date.setProperty(u"fixedSize", QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.btn_next_date)

        self.horizontalLayout_2.addWidget(self.date_control_container)

        self.horizontalSpacer_Right = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_Right)

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
                                         "background : #3388FF;\n"
                                         "border: none;\n"
                                         "padding: 5px 10px;\n"
                                         "font: 700 12px \"Segoe UI\";\n"
                                         "border-radius: 7px")
        self.invteCode_box.setIconSize(QSize(15, 15))

        self.horizontalLayout_2.addWidget(self.invteCode_box)

        self.verticalLayout.addWidget(self.widget)

        self.students_stacked = QStackedWidget(attendance_page)
        self.students_stacked.setObjectName(u"students_stacked")
        self.students_stacked.setStyleSheet(u"background-color: transparent;\n"
                                            "border:none")
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
        self.all_student.setStyleSheet(u"\n"
                                       "#all_student{background-color: rgb(255, 255, 255);\n"
                                       "border:1px solid rgb(187, 187, 187); border-radius: 10px}")
        self.verticalLayout_3 = QVBoxLayout(self.all_student)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.all_student)
        self.frame.setObjectName(u"frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setStyleSheet(u"QLabel{\n"
                                 "	color: #383838;\n"
                                 "	font: 600 9pt \"Segoe UI\";\n"
                                 "}\n"
                                 "")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 12, -1, 9)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(70, 0))
        self.label_3.setStyleSheet(u"")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setMaximumSize(QSize(400, 400))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy4)
        self.label_6.setMinimumSize(QSize(130, 0))
        self.label_6.setMaximumSize(QSize(130, 16777215))

        self.horizontalLayout.addWidget(self.label_6)

        self.verticalLayout_3.addWidget(self.frame)

        self.scrollArea = QScrollArea(self.all_student)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.widget_3 = QWidget()
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(0, 0, 806, 432))
        self.studentsLayout = QVBoxLayout(self.widget_3)
        self.studentsLayout.setSpacing(0)
        self.studentsLayout.setObjectName(u"studentsLayout")
        self.studentsLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 418, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.studentsLayout.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.widget_3)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.students_stacked.addWidget(self.all_student)

        self.verticalLayout.addWidget(self.students_stacked)

        self.retranslateUi(attendance_page)

        self.students_stacked.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(attendance_page)

    # setupUi

    def retranslateUi(self, attendance_page):
        attendance_page.setWindowTitle(QCoreApplication.translate("attendance_page", u"Form", None))
        self.btn_prev_date.setText("")
        self.btn_date_picker.setText(QCoreApplication.translate("attendance_page", u"Today", None))
        self.btn_next_date.setText("")
        self.label.setText(QCoreApplication.translate("attendance_page", u"Invite Code: ", None))
        self.invteCode_box.setText(QCoreApplication.translate("attendance_page", u"AWJDK", None))
        self.label_2.setText(QCoreApplication.translate("attendance_page", u"No students, Invite some!", None))
        self.label_3.setText(QCoreApplication.translate("attendance_page", u"S. No.", None))
        self.label_4.setText(QCoreApplication.translate("attendance_page", u"Name", None))
        self.label_5.setText(QCoreApplication.translate("attendance_page", u"Attendance Rate (in %)", None))
        self.label_6.setText("")
    # retranslateUi
