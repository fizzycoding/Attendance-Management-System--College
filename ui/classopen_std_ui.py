# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'classOpenStd.ui'
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
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_ClassOpenStd(object):
    def setupUi(self, ClassOpenStd):
        if not ClassOpenStd.objectName():
            ClassOpenStd.setObjectName(u"ClassOpenStd")
        ClassOpenStd.resize(1000, 681)
        ClassOpenStd.setStyleSheet(u"background-color: rgb(240, 240, 240); font-family: \"Segoe UI\";")
        self.verticalLayout = QVBoxLayout(ClassOpenStd)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.header_widget = QWidget(ClassOpenStd)
        self.header_widget.setObjectName(u"header_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_widget.sizePolicy().hasHeightForWidth())
        self.header_widget.setSizePolicy(sizePolicy)
        self.header_widget.setStyleSheet(u"background: none;\n"
"border:none")
        self.horizontalLayout = QHBoxLayout(self.header_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.back_btn = QPushButton(self.header_widget)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setMaximumSize(QSize(32, 32))
        self.back_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.back_btn.setStyleSheet(u"border:none; background:transparent;")
        icon = QIcon()
        icon.addFile(u"../icons/back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.back_btn.setIcon(icon)
        self.back_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.back_btn)

        self.class_name = QLabel(self.header_widget)
        self.class_name.setObjectName(u"class_name")
        self.class_name.setStyleSheet(u"color: rgb(34, 34, 34);\n"
"font: 600 16pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.class_name)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.header_widget)

        self.cards_layout = QHBoxLayout()
        self.cards_layout.setSpacing(15)
        self.cards_layout.setObjectName(u"cards_layout")
        self.card_total = QFrame(ClassOpenStd)
        self.card_total.setObjectName(u"card_total")
        self.card_total.setStyleSheet(u"QFrame { background-color: white; border-radius: 10px; border: 1px solid #ddd; }\n"
"QFrame:hover { border: 1px solid #2ab79d; }")
        self.vbox_c1 = QVBoxLayout(self.card_total)
        self.vbox_c1.setObjectName(u"vbox_c1")
        self.lbl_t1 = QLabel(self.card_total)
        self.lbl_t1.setObjectName(u"lbl_t1")

        self.vbox_c1.addWidget(self.lbl_t1)

        self.val_total_classes = QLabel(self.card_total)
        self.val_total_classes.setObjectName(u"val_total_classes")
        self.val_total_classes.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.vbox_c1.addWidget(self.val_total_classes)


        self.cards_layout.addWidget(self.card_total)

        self.card_present = QFrame(ClassOpenStd)
        self.card_present.setObjectName(u"card_present")
        self.card_present.setStyleSheet(u"QFrame { background-color: white; border-radius: 10px; border: 1px solid #ddd; }\n"
"QFrame:hover { border: 1px solid #2ab79d; }")
        self.vbox_c2 = QVBoxLayout(self.card_present)
        self.vbox_c2.setObjectName(u"vbox_c2")
        self.lbl_t2 = QLabel(self.card_present)
        self.lbl_t2.setObjectName(u"lbl_t2")

        self.vbox_c2.addWidget(self.lbl_t2)

        self.val_present = QLabel(self.card_present)
        self.val_present.setObjectName(u"val_present")
        self.val_present.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.vbox_c2.addWidget(self.val_present)


        self.cards_layout.addWidget(self.card_present)

        self.card_absent = QFrame(ClassOpenStd)
        self.card_absent.setObjectName(u"card_absent")
        self.card_absent.setStyleSheet(u"QFrame { background-color: white; border-radius: 10px; border: 1px solid #ddd; }\n"
"QFrame:hover { border: 1px solid #2ab79d; }")
        self.vbox_c3 = QVBoxLayout(self.card_absent)
        self.vbox_c3.setObjectName(u"vbox_c3")
        self.lbl_t3 = QLabel(self.card_absent)
        self.lbl_t3.setObjectName(u"lbl_t3")

        self.vbox_c3.addWidget(self.lbl_t3)

        self.val_absent = QLabel(self.card_absent)
        self.val_absent.setObjectName(u"val_absent")
        self.val_absent.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.vbox_c3.addWidget(self.val_absent)


        self.cards_layout.addWidget(self.card_absent)

        self.card_rate = QFrame(ClassOpenStd)
        self.card_rate.setObjectName(u"card_rate")
        self.card_rate.setStyleSheet(u"QFrame { background-color: white; border-radius: 10px; border: 1px solid #ddd; }\n"
"QFrame:hover { border: 1px solid #2ab79d; }")
        self.vbox_c4 = QVBoxLayout(self.card_rate)
        self.vbox_c4.setObjectName(u"vbox_c4")
        self.lbl_t4 = QLabel(self.card_rate)
        self.lbl_t4.setObjectName(u"lbl_t4")

        self.vbox_c4.addWidget(self.lbl_t4)

        self.val_rate = QLabel(self.card_rate)
        self.val_rate.setObjectName(u"val_rate")
        self.val_rate.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.vbox_c4.addWidget(self.val_rate)


        self.cards_layout.addWidget(self.card_rate)

        self.card_today = QFrame(ClassOpenStd)
        self.card_today.setObjectName(u"card_today")
        self.card_today.setStyleSheet(u"QFrame { background-color: white; border-radius: 10px; border: 1px solid #ddd; }\n"
"QFrame:hover { border: 1px solid #2ab79d; }")
        self.vbox_c5 = QVBoxLayout(self.card_today)
        self.vbox_c5.setObjectName(u"vbox_c5")
        self.lbl_t5 = QLabel(self.card_today)
        self.lbl_t5.setObjectName(u"lbl_t5")

        self.vbox_c5.addWidget(self.lbl_t5)

        self.val_today = QLabel(self.card_today)
        self.val_today.setObjectName(u"val_today")
        self.val_today.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.vbox_c5.addWidget(self.val_today)


        self.cards_layout.addWidget(self.card_today)


        self.verticalLayout.addLayout(self.cards_layout)

        self.student_stack = QStackedWidget(ClassOpenStd)
        self.student_stack.setObjectName(u"student_stack")
        self.all_students = QWidget()
        self.all_students.setObjectName(u"all_students")
        self.verticalLayout_2 = QVBoxLayout(self.all_students)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.all_students)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QLabel{\n"
"	color: #383838;\n"
"	font: 600 9pt \"Segoe UI\";\n"
"}\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(60, 0))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(150, 16777215))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(180, 16777215))
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_6)


        self.verticalLayout_2.addWidget(self.frame)

        self.scrollArea = QScrollArea(self.all_students)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 960, 467))
        self.studentLayout = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.studentLayout.setSpacing(0)
        self.studentLayout.setObjectName(u"studentLayout")
        self.studentLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.studentLayout.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.student_stack.addWidget(self.all_students)
        self.no_student = QWidget()
        self.no_student.setObjectName(u"no_student")
        self.verticalLayout_3 = QVBoxLayout(self.no_student)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.no_student)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.student_stack.addWidget(self.no_student)

        self.verticalLayout.addWidget(self.student_stack)


        self.retranslateUi(ClassOpenStd)

        self.student_stack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ClassOpenStd)
    # setupUi

    def retranslateUi(self, ClassOpenStd):
        ClassOpenStd.setWindowTitle(QCoreApplication.translate("ClassOpenStd", u"Class Details", None))
        self.class_name.setText(QCoreApplication.translate("ClassOpenStd", u"Class Name", None))
        self.lbl_t1.setStyleSheet(QCoreApplication.translate("ClassOpenStd", u"color: #777; font-weight: bold; font-size: 12px; border:none;", None))
        self.lbl_t1.setText(QCoreApplication.translate("ClassOpenStd", u"Total Classes", None))
        self.val_total_classes.setStyleSheet(QCoreApplication.translate("ClassOpenStd", u"color: #333; font-size: 24px; font-weight: bold; border:none;", None))
        self.val_total_classes.setText(QCoreApplication.translate("ClassOpenStd", u"0", None))
        self.lbl_t2.setStyleSheet(QCoreApplication.translate("ClassOpenStd", u"color: #777; font-weight: bold; font-size: 12px; border:none;", None))
        self.lbl_t2.setText(QCoreApplication.translate("ClassOpenStd", u"Present", None))
        self.val_present.setStyleSheet(QCoreApplication.translate("ClassOpenStd", u"color: #2ab79d; font-size: 24px; font-weight: bold; border:none;", None))
        self.val_present.setText(QCoreApplication.translate("ClassOpenStd", u"0", None))
        self.lbl_t3.setStyleSheet(QCoreApplication.translate("ClassOpenStd", u"color: #777; font-weight: bold; font-size: 12px; border:none;", None))
        self.lbl_t3.setText(QCoreApplication.translate("ClassOpenStd", u"Absent", None))
        self.val_absent.setStyleSheet(QCoreApplication.translate("ClassOpenStd", u"color: #ff5252; font-size: 24px; font-weight: bold; border:none;", None))
        self.val_absent.setText(QCoreApplication.translate("ClassOpenStd", u"0", None))
        self.lbl_t4.setStyleSheet(QCoreApplication.translate("ClassOpenStd", u"color: #777; font-weight: bold; font-size: 12px; border:none;", None))
        self.lbl_t4.setText(QCoreApplication.translate("ClassOpenStd", u"Attendance Rate", None))
        self.val_rate.setStyleSheet(QCoreApplication.translate("ClassOpenStd", u"color: #333; font-size: 24px; font-weight: bold; border:none;", None))
        self.val_rate.setText(QCoreApplication.translate("ClassOpenStd", u"0%", None))
        self.lbl_t5.setStyleSheet(QCoreApplication.translate("ClassOpenStd", u"color: #777; font-weight: bold; font-size: 12px; border:none;", None))
        self.lbl_t5.setText(QCoreApplication.translate("ClassOpenStd", u"Today's Status", None))
        self.val_today.setStyleSheet(QCoreApplication.translate("ClassOpenStd", u"color: #555; font-size: 24px; font-weight: bold; border:none;", None))
        self.val_today.setText(QCoreApplication.translate("ClassOpenStd", u"--", None))
        self.student_stack.setStyleSheet(QCoreApplication.translate("ClassOpenStd", u"background:transparent;", None))
        self.label_3.setText(QCoreApplication.translate("ClassOpenStd", u"S.No", None))
        self.label_4.setText(QCoreApplication.translate("ClassOpenStd", u"Name", None))
        self.label_5.setText(QCoreApplication.translate("ClassOpenStd", u"Attendance Rate", None))
        self.label_6.setText(QCoreApplication.translate("ClassOpenStd", u"Status", None))
        self.scrollArea.setStyleSheet(QCoreApplication.translate("ClassOpenStd", u"border:none; background:transparent;", None))
        self.label.setStyleSheet(QCoreApplication.translate("ClassOpenStd", u"font: 16pt \"Segoe UI\"; color: #999;", None))
        self.label.setText(QCoreApplication.translate("ClassOpenStd", u"No students joined yet.", None))
    # retranslateUi

