# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'studentAttendance.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QProgressBar,
    QPushButton,
    QSizePolicy,
    QWidget,
)


class Ui_student_block(object):
    def setupUi(self, student_block):
        if not student_block.objectName():
            student_block.setObjectName("student_block")
        student_block.resize(950, 55)
        student_block.setMinimumSize(QSize(0, 50))
        student_block.setMaximumSize(QSize(16777215, 55))
        student_block.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        student_block.setStyleSheet(
            "QProgressBar {\n"
            "    border-radius:4px;\n"
            "	background-color: rgb(208, 208, 208);\n"
            "	text-align: center;\n"
            "	color: transparent;\n"
            "}\n"
            "QProgressBar::chunk {\n"
            "    border-radius: 4px;\n"
            "    background-color: rgb(42, 183, 157);   }\n"
            "\n"
            "QLabel{\n"
            "	color: rgb(0, 0, 0);\n"
            "}\n"
            "\n"
            "#student_block{\n"
            "	border-top: 1px solid rgb(166, 166, 166);\n"
            "}\n"
            ""
        )
        self.horizontalLayout = QHBoxLayout(student_block)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 5, 0, 5)
        self.serial_number = QLabel(student_block)
        self.serial_number.setObjectName("serial_number")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.serial_number.sizePolicy().hasHeightForWidth()
        )
        self.serial_number.setSizePolicy(sizePolicy)
        self.serial_number.setMinimumSize(QSize(70, 0))
        self.serial_number.setMaximumSize(QSize(60, 16777215))
        self.serial_number.setStyleSheet(
            "\n" "color: rgb(47, 47, 47);\n" 'font: 600 12pt "Segoe UI";'
        )
        self.serial_number.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.serial_number)

        self.name = QPushButton(student_block)
        self.name.setObjectName("name")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy1)
        self.name.setStyleSheet(
            "color: rgb(15, 15, 15);\n"
            'font: 600 12pt "Segoe UI";\n'
            "text-align: left;\n"
            "padding: 0px;\n"
            "border: none"
        )

        self.horizontalLayout.addWidget(self.name)

        self.widget_2 = QWidget(student_block)
        self.widget_2.setObjectName("widget_2")
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.widget_2.setMinimumSize(QSize(0, 8))
        self.widget_2.setMaximumSize(QSize(400, 16777215))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.progressBar_attendance_rate = QProgressBar(self.widget_2)
        self.progressBar_attendance_rate.setObjectName("progressBar_attendance_rate")
        sizePolicy1.setHeightForWidth(
            self.progressBar_attendance_rate.sizePolicy().hasHeightForWidth()
        )
        self.progressBar_attendance_rate.setSizePolicy(sizePolicy1)
        self.progressBar_attendance_rate.setMinimumSize(QSize(0, 0))
        self.progressBar_attendance_rate.setMaximumSize(QSize(300, 8))
        self.progressBar_attendance_rate.setStyleSheet("")
        self.progressBar_attendance_rate.setValue(50)

        self.horizontalLayout_3.addWidget(self.progressBar_attendance_rate)

        self.attendance_rate_label = QLabel(self.widget_2)
        self.attendance_rate_label.setObjectName("attendance_rate_label")
        sizePolicy.setHeightForWidth(
            self.attendance_rate_label.sizePolicy().hasHeightForWidth()
        )
        self.attendance_rate_label.setSizePolicy(sizePolicy)
        self.attendance_rate_label.setMaximumSize(QSize(60, 16777215))
        self.attendance_rate_label.setStyleSheet(
            'font: 600 12pt "Segoe UI";\n' "color: rgb(36, 36, 36);"
        )

        self.horizontalLayout_3.addWidget(self.attendance_rate_label)

        self.horizontalLayout.addWidget(self.widget_2)

        self.widget = QWidget(student_block)
        self.widget.setObjectName("widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QSize(130, 16777215))
        self.widget.setStyleSheet("QPushButton{\n" "	border: none\n" "}")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_present = QPushButton(self.widget)
        self.btn_present.setObjectName("btn_present")
        sizePolicy.setHeightForWidth(self.btn_present.sizePolicy().hasHeightForWidth())
        self.btn_present.setSizePolicy(sizePolicy)
        self.btn_present.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(
            "icons/present_unchecked.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.btn_present.setIcon(icon)
        self.btn_present.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btn_present)

        self.btn_absent = QPushButton(self.widget)
        self.btn_absent.setObjectName("btn_absent")
        sizePolicy.setHeightForWidth(self.btn_absent.sizePolicy().hasHeightForWidth())
        self.btn_absent.setSizePolicy(sizePolicy)
        self.btn_absent.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(
            "icons/absent_unchecked.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.btn_absent.setIcon(icon1)
        self.btn_absent.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btn_absent)

        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(student_block)

        QMetaObject.connectSlotsByName(student_block)

    # setupUi

    def retranslateUi(self, student_block):
        student_block.setWindowTitle(
            QCoreApplication.translate("student_block", "Form", None)
        )
        self.serial_number.setText(
            QCoreApplication.translate("student_block", "001", None)
        )
        self.name.setText(
            QCoreApplication.translate("student_block", "Sanju Patel", None)
        )
        self.attendance_rate_label.setText(
            QCoreApplication.translate("student_block", "100%", None)
        )
        self.btn_present.setText("")
        self.btn_absent.setText("")

    # retranslateUi
