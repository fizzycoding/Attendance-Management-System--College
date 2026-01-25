# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_details_page.ui'
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
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class Ui_test_details_page(object):
    def setupUi(self, test_details_page):
        if not test_details_page.objectName():
            test_details_page.setObjectName("test_details_page")
        test_details_page.resize(842, 562)
        test_details_page.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.verticalLayout = QVBoxLayout(test_details_page)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header_widget = QWidget(test_details_page)
        self.header_widget.setObjectName("header_widget")
        self.header_widget.setStyleSheet("background-color: transparent;")
        self.horizontalLayout_header = QHBoxLayout(self.header_widget)
        self.horizontalLayout_header.setObjectName("horizontalLayout_header")
        self.horizontalLayout_header.setContentsMargins(0, 0, 0, 0)
        self.btn_back = QPushButton(self.header_widget)
        self.btn_back.setObjectName("btn_back")
        self.btn_back.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_back.setStyleSheet(
            "\n"
            "          QPushButton {\n"
            "           border: none;\n"
            "           border-radius: 20px;\n"
            "           padding: 5px;\n"
            "          }\n"
            "          QPushButton:hover {\n"
            "           background-color: #e0e0e0;\n"
            "          }\n"
            "         "
        )
        icon = QIcon()
        icon.addFile("icons/back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_back.setIcon(icon)
        self.btn_back.setIconSize(QSize(24, 24))
        self.btn_back.setProperty("fixedSize", QSize(40, 40))

        self.horizontalLayout_header.addWidget(self.btn_back)

        self.info_container = QWidget(self.header_widget)
        self.info_container.setObjectName("info_container")
        self.verticalLayout_info = QVBoxLayout(self.info_container)
        self.verticalLayout_info.setSpacing(2)
        self.verticalLayout_info.setObjectName("verticalLayout_info")
        self.verticalLayout_info.setContentsMargins(10, -1, -1, -1)
        self.label_test_name = QLabel(self.info_container)
        self.label_test_name.setObjectName("label_test_name")
        self.label_test_name.setStyleSheet('font: 700 16pt "Segoe UI"; color: #333;')

        self.verticalLayout_info.addWidget(self.label_test_name)

        self.details_row = QWidget(self.info_container)
        self.details_row.setObjectName("details_row")
        self.horizontalLayout_details = QHBoxLayout(self.details_row)
        self.horizontalLayout_details.setSpacing(15)
        self.horizontalLayout_details.setObjectName("horizontalLayout_details")
        self.horizontalLayout_details.setContentsMargins(0, 0, -1, 0)
        self.label_max = QLabel(self.details_row)
        self.label_max.setObjectName("label_max")
        self.label_max.setStyleSheet('font: 10pt "Segoe UI"; color: #666;')

        self.horizontalLayout_details.addWidget(self.label_max)

        self.label_pass = QLabel(self.details_row)
        self.label_pass.setObjectName("label_pass")
        self.label_pass.setStyleSheet('font: 10pt "Segoe UI"; color: #666;')

        self.horizontalLayout_details.addWidget(self.label_pass)

        self.label_date = QLabel(self.details_row)
        self.label_date.setObjectName("label_date")
        self.label_date.setStyleSheet('font: 10pt "Segoe UI"; color: #666;')

        self.horizontalLayout_details.addWidget(self.label_date)

        self.horizontalSpacer_details = QSpacerItem(
            0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_details.addItem(self.horizontalSpacer_details)

        self.verticalLayout_info.addWidget(self.details_row)

        self.horizontalLayout_header.addWidget(self.info_container)

        self.horizontalSpacer_main = QSpacerItem(
            0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_header.addItem(self.horizontalSpacer_main)

        self.btn_save_marks = QPushButton(self.header_widget)
        self.btn_save_marks.setObjectName("btn_save_marks")
        self.btn_save_marks.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_save_marks.setStyleSheet(
            "\n"
            "color: #fff;\n"
            "background : #3388FF;\n"
            "border: none;\n"
            "padding: 10px 20px;\n"
            'font: 600 14px "Segoe UI";\n'
            "border-radius: 7px"
        )
        icon1 = QIcon()
        icon1.addFile("icons/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_save_marks.setIcon(icon1)

        self.horizontalLayout_header.addWidget(self.btn_save_marks)

        self.verticalLayout.addWidget(self.header_widget)

        self.scrollArea = QScrollArea(test_details_page)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setStyleSheet("background-color: transparent;\n" "")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 824, 468))
        self.studentsLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.studentsLayout.setSpacing(0)
        self.studentsLayout.setObjectName("studentsLayout")
        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.studentsLayout.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(test_details_page)

        QMetaObject.connectSlotsByName(test_details_page)

    # setupUi

    def retranslateUi(self, test_details_page):
        test_details_page.setWindowTitle(
            QCoreApplication.translate("test_details_page", "Test Details", None)
        )
        self.btn_back.setText("")
        self.label_test_name.setText(
            QCoreApplication.translate("test_details_page", "Unit Test 1", None)
        )
        self.label_max.setText(
            QCoreApplication.translate("test_details_page", "Max Marks: 50", None)
        )
        self.label_pass.setText(
            QCoreApplication.translate("test_details_page", "Min Marks: 17", None)
        )
        self.label_date.setText(
            QCoreApplication.translate("test_details_page", "Date: 28-Dec-2025", None)
        )
        self.btn_save_marks.setText(
            QCoreApplication.translate("test_details_page", "Save Marks", None)
        )

    # retranslateUi
