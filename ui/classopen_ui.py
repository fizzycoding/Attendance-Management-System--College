# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'classOpen.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QRect,
    QSize,
    Qt,
)
from PySide6.QtGui import (
    QCursor,
    QIcon,
)
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_ClassOpen(object):
    def setupUi(self, ClassOpen):
        if not ClassOpen.objectName():
            ClassOpen.setObjectName("ClassOpen")
        ClassOpen.resize(908, 658)
        ClassOpen.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.verticalLayout = QVBoxLayout(ClassOpen)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QWidget(ClassOpen)
        self.widget.setObjectName("widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet("background-color: transparent;")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back_btn = QPushButton(self.widget)
        self.back_btn.setObjectName("back_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.back_btn.sizePolicy().hasHeightForWidth())
        self.back_btn.setSizePolicy(sizePolicy1)
        self.back_btn.setMaximumSize(QSize(32, 32))
        self.back_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.back_btn.setStyleSheet("border:none")
        icon = QIcon()
        icon.addFile("icons/back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.back_btn.setIcon(icon)
        self.back_btn.setIconSize(QSize(22, 22))

        self.horizontalLayout.addWidget(self.back_btn)

        self.class_name = QLabel(self.widget)
        self.class_name.setObjectName("class_name")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.class_name.sizePolicy().hasHeightForWidth())
        self.class_name.setSizePolicy(sizePolicy2)
        self.class_name.setStyleSheet(
            "color: rgb(34, 34, 34);\n" 'font: 600 16pt "Segoe UI";'
        )

        self.horizontalLayout.addWidget(self.class_name)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n" "border: none")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.invite_code = QPushButton(self.widget_2)
        self.invite_code.setObjectName("invite_code")
        sizePolicy1.setHeightForWidth(self.invite_code.sizePolicy().hasHeightForWidth())
        self.invite_code.setSizePolicy(sizePolicy1)
        self.invite_code.setStyleSheet(
            "color: #159079;\n" "border: none;\n" 'font: 700 12pt "Segoe UI";'
        )

        self.horizontalLayout_3.addWidget(self.invite_code)

        self.horizontalLayout.addWidget(self.widget_2)

        self.verticalLayout.addWidget(self.widget)

        self.student_stack = QStackedWidget(ClassOpen)
        self.student_stack.setObjectName("student_stack")
        self.student_stack.setStyleSheet(
            "background-color: transparent;\n" "border:none"
        )
        self.all_students = QWidget()
        self.all_students.setObjectName("all_students")
        self.verticalLayout_2 = QVBoxLayout(self.all_students)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.all_students)
        self.frame.setObjectName("frame")
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum
        )
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setStyleSheet(
            "QLabel{\n" "	color: #383838;\n" '	font: 600 9pt "Segoe UI";\n' "}\n" ""
        )
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 9, -1, 0)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(70, 0))
        self.label_3.setStyleSheet("")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName("label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        sizePolicy4 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)
        self.label_5.setMaximumSize(QSize(450, 450))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setMinimumSize(QSize(190, 0))
        self.label_6.setMaximumSize(QSize(180, 16777215))

        self.horizontalLayout_2.addWidget(self.label_6)

        self.verticalLayout_2.addWidget(self.frame)

        self.scrollArea = QScrollArea(self.all_students)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 890, 551))
        self.studentLayout = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.studentLayout.setObjectName("studentLayout")
        self.verticalSpacer = QSpacerItem(
            20, 530, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.studentLayout.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.student_stack.addWidget(self.all_students)
        self.no_student = QWidget()
        self.no_student.setObjectName("no_student")
        self.verticalLayout_3 = QVBoxLayout(self.no_student)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QLabel(self.no_student)
        self.label.setObjectName("label")
        self.label.setStyleSheet(
            "QLabel{\n" '  font: 15pt "Segoe UI";\n' "  color: rgb(0, 0, 0);\n" "}"
        )
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.student_stack.addWidget(self.no_student)

        self.verticalLayout.addWidget(self.student_stack)

        self.retranslateUi(ClassOpen)

        QMetaObject.connectSlotsByName(ClassOpen)

    # setupUi

    def retranslateUi(self, ClassOpen):
        ClassOpen.setWindowTitle(QCoreApplication.translate("ClassOpen", "Form", None))
        self.back_btn.setText("")
        self.class_name.setText(
            QCoreApplication.translate("ClassOpen", "BCA 3rd year", None)
        )
        self.label_2.setText(
            QCoreApplication.translate("ClassOpen", "Invite Code: ", None)
        )
        self.invite_code.setText(QCoreApplication.translate("ClassOpen", "23232", None))
        self.label_3.setText(QCoreApplication.translate("ClassOpen", "S. No.", None))
        self.label_4.setText(QCoreApplication.translate("ClassOpen", "Name", None))
        self.label_5.setText(
            QCoreApplication.translate("ClassOpen", "Attendance Rate (in %)", None)
        )
        self.label_6.setText(
            QCoreApplication.translate("ClassOpen", "Attendance", None)
        )
        self.label.setText(
            QCoreApplication.translate("ClassOpen", "No students, Invite some!", None)
        )

    # retranslateUi
