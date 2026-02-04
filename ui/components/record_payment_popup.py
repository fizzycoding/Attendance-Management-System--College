# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recordPaymentPopup.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_RecordPaymentPopup(object):
    def setupUi(self, RecordPaymentPopup):
        if not RecordPaymentPopup.objectName():
            RecordPaymentPopup.setObjectName(u"RecordPaymentPopup")
        RecordPaymentPopup.resize(400, 280)
        RecordPaymentPopup.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(RecordPaymentPopup)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.backgroundFrame = QFrame(RecordPaymentPopup)
        self.backgroundFrame.setObjectName(u"backgroundFrame")
        self.backgroundFrame.setStyleSheet(u"\n"
"                            #backgroundFrame {\n"
"                            background-color: white;\n"
"                            }\n"
"\n"
"                            QLabel {\n"
"                            color: #333;\n"
"                            font-family: \"Segoe UI\";\n"
"                            font-size: 20px;\n"
"                            font-weight: bold;\n"
"                            border: none;\n"
"                            }\n"
"\n"
"                            QPushButton {\n"
"                            height: 35px;\n"
"                            padding: 0 16px;\n"
"                            background-color: #3388FF;\n"
"                            color: white;\n"
"                            font-size: 14px;\n"
"                            font-weight: 600;\n"
"                            border: none;\n"
"                            border-radius: 5px;\n"
"                            }\n"
"\n"
"                            QPushButton:hover {\n"
"         "
                        "                   background-color: #0055FF;\n"
"                            }\n"
"                        ")
        self.mainContentLayout = QVBoxLayout(self.backgroundFrame)
        self.mainContentLayout.setSpacing(16)
        self.mainContentLayout.setObjectName(u"mainContentLayout")
        self.mainContentLayout.setContentsMargins(18, 18, 18, 18)
        self.titleLabel = QLabel(self.backgroundFrame)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mainContentLayout.addWidget(self.titleLabel)

        self.infoWidget = QWidget(self.backgroundFrame)
        self.infoWidget.setObjectName(u"infoWidget")
        self.infoWidget.setStyleSheet(u"\n"
"                                        QLabel {\n"
"                                        color: #111;\n"
"                                        font: 600 9pt \"Segoe UI\";\n"
"                                        }\n"
"\n"
"                                        #valueLabel {\n"
"                                        font: 500 9pt \"Segoe UI\";\n"
"                                        color: #444;\n"
"                                        }\n"
"                                    ")
        self.infoLayout = QVBoxLayout(self.infoWidget)
        self.infoLayout.setSpacing(6)
        self.infoLayout.setObjectName(u"infoLayout")
        self.studentNameLabel = QLabel(self.infoWidget)
        self.studentNameLabel.setObjectName(u"studentNameLabel")

        self.infoLayout.addWidget(self.studentNameLabel)

        self.pendingAmountLabel = QLabel(self.infoWidget)
        self.pendingAmountLabel.setObjectName(u"pendingAmountLabel")

        self.infoLayout.addWidget(self.pendingAmountLabel)


        self.mainContentLayout.addWidget(self.infoWidget)

        self.inputWidget = QWidget(self.backgroundFrame)
        self.inputWidget.setObjectName(u"inputWidget")
        self.inputWidget.setStyleSheet(u"\n"
"                                        QLabel{color : rgb(0,0,0);font: 600 8pt \"Segoe UI\";}\n"
"\n"
"                                        QLineEdit {\n"
"                                        height: 20px;\n"
"                                        padding: 8px 10px;\n"
"                                        font-size: 14px;\n"
"                                        color: #111;\n"
"                                        border: 1px solid rgb(99, 99, 99);\n"
"                                        background: #fff;\n"
"                                        border-radius: 4px;\n"
"                                        }\n"
"\n"
"                                        QLineEdit:focus {\n"
"                                        border: 1.5px solid #3388FF;\n"
"                                        }\n"
"                                    ")
        self.verticalLayout_3 = QVBoxLayout(self.inputWidget)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.amountLabel = QLabel(self.inputWidget)
        self.amountLabel.setObjectName(u"amountLabel")

        self.verticalLayout_3.addWidget(self.amountLabel)

        self.payment_input = QLineEdit(self.inputWidget)
        self.payment_input.setObjectName(u"payment_input")

        self.verticalLayout_3.addWidget(self.payment_input)


        self.mainContentLayout.addWidget(self.inputWidget)

        self.buttonsWidget = QWidget(self.backgroundFrame)
        self.buttonsWidget.setObjectName(u"buttonsWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.buttonsWidget)
        self.horizontalLayout_2.setSpacing(18)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cancelBtn = QPushButton(self.buttonsWidget)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cancelBtn.setStyleSheet(u"\n"
"                                                    QPushButton {\n"
"                                                    background-color: rgb(255, 255, 255);\n"
"                                                    color: #333;\n"
"                                                    border: 1px solid #333;\n"
"                                                    border-radius: 5px;\n"
"                                                    }\n"
"\n"
"                                                    QPushButton:hover {\n"
"                                                    background-color: rgba(51, 51, 51, 30);\n"
"                                                    }\n"
"\n"
"                                                    QPushButton:pressed {\n"
"                                                    background-color: rgba(51, 51, 51, 80);\n"
"                                                    }\n"
"                                                ")

        self.horizontalLayout_2.addWidget(self.cancelBtn)

        self.recordBtn = QPushButton(self.buttonsWidget)
        self.recordBtn.setObjectName(u"recordBtn")
        self.recordBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.recordBtn)


        self.mainContentLayout.addWidget(self.buttonsWidget)


        self.verticalLayout.addWidget(self.backgroundFrame)


        self.retranslateUi(RecordPaymentPopup)

        QMetaObject.connectSlotsByName(RecordPaymentPopup)
    # setupUi

    def retranslateUi(self, RecordPaymentPopup):
        RecordPaymentPopup.setWindowTitle(QCoreApplication.translate("RecordPaymentPopup", u"Record Payment", None))
        self.titleLabel.setText(QCoreApplication.translate("RecordPaymentPopup", u"Record Payment", None))
        self.studentNameLabel.setText(QCoreApplication.translate("RecordPaymentPopup", u"Student: --", None))
        self.pendingAmountLabel.setText(QCoreApplication.translate("RecordPaymentPopup", u"Pending: \u20b90", None))
        self.amountLabel.setText(QCoreApplication.translate("RecordPaymentPopup", u"Enter Paid Amount", None))
        self.payment_input.setPlaceholderText(QCoreApplication.translate("RecordPaymentPopup", u"e.g. 500", None))
        self.cancelBtn.setText(QCoreApplication.translate("RecordPaymentPopup", u"Cancel", None))
        self.recordBtn.setText(QCoreApplication.translate("RecordPaymentPopup", u"Record", None))
    # retranslateUi

