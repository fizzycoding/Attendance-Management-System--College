# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testResults.ui'
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
    QComboBox,
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


class Ui_tests_page(object):
    def setupUi(self, tests_page):
        if not tests_page.objectName():
            tests_page.setObjectName("tests_page")
        tests_page.resize(842, 562)
        tests_page.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.verticalLayout = QVBoxLayout(tests_page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header_widget = QWidget(tests_page)
        self.header_widget.setObjectName("header_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.header_widget.sizePolicy().hasHeightForWidth()
        )
        self.header_widget.setSizePolicy(sizePolicy)
        self.header_widget.setStyleSheet("background-color: transparent")
        self.horizontalLayout_2 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dropdown_classes = QComboBox(self.header_widget)
        self.dropdown_classes.setObjectName("dropdown_classes")
        self.dropdown_classes.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.dropdown_classes.sizePolicy().hasHeightForWidth()
        )
        self.dropdown_classes.setSizePolicy(sizePolicy1)
        self.dropdown_classes.setMinimumSize(QSize(0, 0))
        self.dropdown_classes.setStyleSheet(
            "QComboBox {\n"
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
            "}"
        )

        self.horizontalLayout_2.addWidget(self.dropdown_classes)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_new_test = QPushButton(self.header_widget)
        self.btn_new_test.setObjectName("btn_new_test")
        self.btn_new_test.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_new_test.setStyleSheet(
            "color: #fff;\n"
            "background : qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(42, 183, 157), stop:1 #067d68);;\n"
            "border: none;\n"
            "padding: 10px 20px;\n"
            'font: 800 14px "Segoe UI";\n'
            "border-radius: 7px"
        )
        icon = QIcon()
        icon.addFile("icons/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_new_test.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.btn_new_test)

        self.verticalLayout.addWidget(self.header_widget)

        self.content_stack = QStackedWidget(tests_page)
        self.content_stack.setObjectName("content_stack")
        self.content_stack.setStyleSheet("background-color: transparent")
        self.page_no_test = QWidget()
        self.page_no_test.setObjectName("page_no_test")
        self.verticalLayout_empty = QVBoxLayout(self.page_no_test)
        self.verticalLayout_empty.setObjectName("verticalLayout_empty")
        self.label_no_test = QLabel(self.page_no_test)
        self.label_no_test.setObjectName("label_no_test")
        self.label_no_test.setStyleSheet(
            'font: 15pt "Segoe UI"; color: rgb(100, 100, 100);'
        )
        self.label_no_test.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_empty.addWidget(self.label_no_test)

        self.content_stack.addWidget(self.page_no_test)
        self.page_list = QWidget()
        self.page_list.setObjectName("page_list")
        self.verticalLayout_list = QVBoxLayout(self.page_list)
        self.verticalLayout_list.setObjectName("verticalLayout_list")
        self.verticalLayout_list.setContentsMargins(0, 0, 0, 0)
        self.test_list_container = QScrollArea(self.page_list)
        self.test_list_container.setObjectName("test_list_container")
        self.test_list_container.setFrameShape(QFrame.Shape.NoFrame)
        self.test_list_container.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 824, 481))
        self.testsLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.testsLayout.setObjectName("testsLayout")
        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.testsLayout.addItem(self.verticalSpacer)

        self.test_list_container.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_list.addWidget(self.test_list_container)

        self.content_stack.addWidget(self.page_list)

        self.verticalLayout.addWidget(self.content_stack)

        self.retranslateUi(tests_page)

        self.content_stack.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(tests_page)

    # setupUi

    def retranslateUi(self, tests_page):
        tests_page.setWindowTitle(
            QCoreApplication.translate("tests_page", "Tests Dashboard", None)
        )
        self.btn_new_test.setText(
            QCoreApplication.translate("tests_page", "Create New Test", None)
        )
        self.label_no_test.setText(
            QCoreApplication.translate("tests_page", "No Tests Created Yet!", None)
        )

    # retranslateUi
