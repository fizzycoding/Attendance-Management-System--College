from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QSize,
    Qt,
)
from PySide6.QtGui import (
    QIcon,
)
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class Ui_FeeTransactionCard(object):
    def setupUi(self, FeeTransactionCard):
        if not FeeTransactionCard.objectName():
            FeeTransactionCard.setObjectName("FeeTransactionCard")
        FeeTransactionCard.resize(1170, 62)
        FeeTransactionCard.setMinimumSize(QSize(0, 62))
        FeeTransactionCard.setStyleSheet(
            "\n"
            "#FeeTransactionCard{\n"
            "    background: white;\n"
            "    border: 1px solid rgb(210,210,210);\n"
            "    border-radius: 10px;\n"
            "}\n"
            "#FeeTransactionCard:hover{\n"
            "    border: 1px solid #3388FF;\n"
            "}\n"
            "\n"
            "QLabel{\n"
            "    border:none;\n"
            '    font-family: "Segoe UI";\n'
            "}\n"
            "   "
        )
        self.mainLayout = QHBoxLayout(FeeTransactionCard)
        self.mainLayout.setSpacing(12)
        self.mainLayout.setObjectName("mainLayout")
        self.mainLayout.setContentsMargins(12, 10, 12, 10)
        self.iconCircle = QFrame(FeeTransactionCard)
        self.iconCircle.setObjectName("iconCircle")
        self.iconCircle.setMinimumSize(QSize(34, 34))
        self.iconCircle.setMaximumSize(QSize(34, 34))
        self.iconCircle.setStyleSheet(
            "\n"
            "#iconCircle{\n"
            "    background-color: rgba(51, 136, 255, 25);\n"
            "    border-radius: 17px;\n"
            "    border:none;\n"
            "}\n"
            "      "
        )
        self.horizontalLayout = QHBoxLayout(self.iconCircle)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.iconCircle)
        self.pushButton.setObjectName("pushButton")
        icon = QIcon()
        icon.addFile("icons/uparrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(19, 19))

        self.horizontalLayout.addWidget(self.pushButton)

        self.mainLayout.addWidget(self.iconCircle)

        self.textContainer = QWidget(FeeTransactionCard)
        self.textContainer.setObjectName("textContainer")
        self.textLayout = QVBoxLayout(self.textContainer)
        self.textLayout.setSpacing(2)
        self.textLayout.setObjectName("textLayout")
        self.textLayout.setContentsMargins(0, 0, 0, 0)
        self.label_title = QLabel(self.textContainer)
        self.label_title.setObjectName("label_title")
        self.label_title.setStyleSheet(
            "font-size: 13px; font-weight: 700; color: #222;"
        )

        self.textLayout.addWidget(self.label_title)

        self.label_datetime = QLabel(self.textContainer)
        self.label_datetime.setObjectName("label_datetime")
        self.label_datetime.setStyleSheet(
            "font-size: 11px; font-weight: 600; color: #777;"
        )

        self.textLayout.addWidget(self.label_datetime)

        self.mainLayout.addWidget(self.textContainer)

        self.rightSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.mainLayout.addItem(self.rightSpacer)

        self.label_amount = QLabel(FeeTransactionCard)
        self.label_amount.setObjectName("label_amount")
        self.label_amount.setStyleSheet(
            "font-size: 14px; font-weight: 800; color: #3388FF;"
        )
        self.label_amount.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.mainLayout.addWidget(self.label_amount)

        self.retranslateUi(FeeTransactionCard)

        QMetaObject.connectSlotsByName(FeeTransactionCard)

    # setupUi

    def retranslateUi(self, FeeTransactionCard):
        self.pushButton.setText("")
        self.label_title.setText(
            QCoreApplication.translate("FeeTransactionCard", "Payment received", None)
        )
        self.label_datetime.setText(
            QCoreApplication.translate("FeeTransactionCard", "--", None)
        )
        self.label_amount.setText(
            QCoreApplication.translate("FeeTransactionCard", "\u20b90", None)
        )
        pass

    # retranslateUi
