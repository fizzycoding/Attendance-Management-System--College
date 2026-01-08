# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testCard.ui'
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
    QSizePolicy,
    QSpacerItem,
    QWidget,
)


class Ui_test_card(object):
    def setupUi(self, test_card):
        if not test_card.objectName():
            test_card.setObjectName("test_card")
        test_card.resize(950, 48)
        test_card.setMinimumSize(QSize(0, 40))
        test_card.setMaximumSize(QSize(16777215, 55))
        test_card.setStyleSheet(
            "#test_card {\n"
            "    border-top: 1px solid rgb(166, 166, 166);\n"
            "    background-color: transparent;\n"
            "}\n"
            "QLabel {\n"
            "    color: rgb(30, 30, 30);\n"
            "    border: none;\n"
            "	background-color: transparent;\n"
            "}"
        )
        self.horizontalLayout = QHBoxLayout(test_card)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 5, 20, 5)
        self.test_name = QLabel(test_card)
        self.test_name.setObjectName("test_name")
        self.test_name.setStyleSheet(
            'font: 600 12pt "Segoe UI"; color: rgb(15, 15, 15);'
        )

        self.horizontalLayout.addWidget(self.test_name)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_max = QLabel(test_card)
        self.label_max.setObjectName("label_max")
        self.label_max.setStyleSheet('font: 10pt "Segoe UI"; color: #555;')

        self.horizontalLayout.addWidget(self.label_max)

        self.label_pass = QLabel(test_card)
        self.label_pass.setObjectName("label_pass")
        self.label_pass.setStyleSheet('font: 10pt "Segoe UI"; color: #555;')

        self.horizontalLayout.addWidget(self.label_pass)

        self.test_date = QLabel(test_card)
        self.test_date.setObjectName("test_date")
        self.test_date.setStyleSheet(
            'font: 10pt "Segoe UI"; color: #777; font-style: italic;'
        )

        self.horizontalLayout.addWidget(self.test_date)

        self.btn_open = QPushButton(test_card)
        self.btn_open.setObjectName("btn_open")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_open.sizePolicy().hasHeightForWidth())
        self.btn_open.setSizePolicy(sizePolicy)
        self.btn_open.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_open.setStyleSheet(
            '#btn_open{background-color: #E0F2F1; color: #009688; border: none; padding: 5px 18px; border-radius: 4px; font-weight: bold; font-family: "Segoe UI";}\n'
            "#btn_open:hover{background-color: rgb(167, 221, 199);}"
        )

        self.horizontalLayout.addWidget(self.btn_open)

        self.btn_delete = QPushButton(test_card)
        self.btn_delete.setObjectName("btn_delete")
        self.btn_delete.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_delete.setStyleSheet(
            "color: #D32F2F; background: transparent; font-size: 16px; border: none;"
        )
        icon = QIcon()
        icon.addFile("icons/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_delete.setIcon(icon)
        self.btn_delete.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_delete)

        self.retranslateUi(test_card)

        QMetaObject.connectSlotsByName(test_card)

    # setupUi

    def retranslateUi(self, test_card):
        self.test_name.setText(
            QCoreApplication.translate("test_card", "Unit Test 1", None)
        )
        self.label_max.setText(QCoreApplication.translate("test_card", "Max: 50", None))
        self.label_pass.setText(
            QCoreApplication.translate("test_card", "Pass: 17", None)
        )
        self.test_date.setText(
            QCoreApplication.translate("test_card", "28-Dec-2025", None)
        )
        self.btn_open.setText(QCoreApplication.translate("test_card", "Open", None))
        self.btn_delete.setText("")
        pass

    # retranslateUi
