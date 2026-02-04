# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'classCard.ui'
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
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QWidget,
)


class Ui_class_card(object):
    def setupUi(self, class_card):
        if not class_card.objectName():
            class_card.setObjectName("class_card")
        class_card.resize(780, 50)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(class_card.sizePolicy().hasHeightForWidth())
        class_card.setSizePolicy(sizePolicy)
        class_card.setMinimumSize(QSize(0, 50))
        class_card.setMaximumSize(QSize(16777215, 50))
        class_card.setStyleSheet(
            "#class_card{\n"
            "    background-color: rgb(255, 255, 255);\n"
            "    border-radius: 7px;\n"
            "    border: 1px solid rgb(166, 166, 166);\n"
            "}\n"
            "\n"
            "#class_card:hover{\n"
            "  background-color: rgba(51, 143, 255, 20);\n"
            "}"
        )
        self.horizontalLayout = QHBoxLayout(class_card)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 1, 20, 1)
        self.class_name = QLabel(class_card)
        self.class_name.setObjectName("class_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.class_name.sizePolicy().hasHeightForWidth())
        self.class_name.setSizePolicy(sizePolicy1)
        self.class_name.setStyleSheet(
            'font: 600 18px "Segoe UI";\n'
            "color: rgb(48, 48, 48);\n"
            "background-color: transparent;"
        )

        self.horizontalLayout.addWidget(self.class_name)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.status_container = QWidget(class_card)
        self.status_container.setObjectName("status_container")
        sizePolicy1.setHeightForWidth(
            self.status_container.sizePolicy().hasHeightForWidth()
        )
        self.status_container.setSizePolicy(sizePolicy1)
        self.status_container.setStyleSheet(
            "QPushButton{\n"
            '  font: 600 12pt "Segoe UI";\n'
            "  color: rgb(39, 39, 39);\n"
            "  background: transparent;\n"
            "  border: none;\n"
            "}\n"
            "#status_container{\n"
            "background-color: transparent;}"
        )
        self.horizontalLayout_3 = QHBoxLayout(self.status_container)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.total_user_label = QPushButton(self.status_container)
        self.total_user_label.setObjectName("total_user_label")
        self.total_user_label.setMinimumSize(QSize(20, 20))
        icon = QIcon()
        icon.addFile("icons/users.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.total_user_label.setIcon(icon)
        self.total_user_label.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.total_user_label)

        self.present_label = QPushButton(self.status_container)
        self.present_label.setObjectName("present_label")
        icon1 = QIcon()
        icon1.addFile("icons/present.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.present_label.setIcon(icon1)
        self.present_label.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.present_label)

        self.absent_label = QPushButton(self.status_container)
        self.absent_label.setObjectName("absent_label")
        icon2 = QIcon()
        icon2.addFile("icons/absent.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.absent_label.setIcon(icon2)
        self.absent_label.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.absent_label)

        self.btn_edit = QPushButton(self.status_container)
        self.btn_edit.setObjectName("btn_edit")
        sizePolicy1.setHeightForWidth(self.btn_edit.sizePolicy().hasHeightForWidth())
        self.btn_edit.setSizePolicy(sizePolicy1)
        self.btn_edit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_edit.setStyleSheet("")
        icon3 = QIcon()
        icon3.addFile("icons/edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_edit.setIcon(icon3)
        self.btn_edit.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.btn_edit)

        self.btn_delete = QPushButton(self.status_container)
        self.btn_delete.setObjectName("btn_delete")
        self.btn_delete.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile("icons/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_delete.setIcon(icon4)
        self.btn_delete.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.btn_delete)

        self.horizontalLayout.addWidget(self.status_container)

        self.retranslateUi(class_card)

        QMetaObject.connectSlotsByName(class_card)

    # setupUi

    def retranslateUi(self, class_card):
        self.class_name.setText(
            QCoreApplication.translate("class_card", "BCA 3rd", None)
        )
        self.total_user_label.setText(
            QCoreApplication.translate("class_card", "10", None)
        )
        self.present_label.setText(
            QCoreApplication.translate("class_card", "150", None)
        )
        self.absent_label.setText(QCoreApplication.translate("class_card", "200", None))
        self.btn_edit.setText("")
        self.btn_delete.setText("")
        pass

    # retranslateUi
