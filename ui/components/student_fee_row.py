# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'studentFeeRow.ui'
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
    QPushButton, QSizePolicy, QWidget)

class Ui_StudentFeeRow(object):
    def setupUi(self, StudentFeeRow):
        if not StudentFeeRow.objectName():
            StudentFeeRow.setObjectName(u"StudentFeeRow")
        StudentFeeRow.resize(866, 50)
        StudentFeeRow.setMinimumSize(QSize(0, 50))
        StudentFeeRow.setMaximumSize(QSize(16777215, 56))
        StudentFeeRow.setStyleSheet(u"\n"
"\n"
"                QLabel {\n"
"                border: none;\n"
"                color: #222;\n"
"                font-size: 14px;\n"
"font-weight: 600\n"
"                }\n"
"\n"
"                QPushButton {\n"
"                border: none;\n"
"                padding: 8px 14px;\n"
"                border-radius: 8px;\n"
"                background-color: #2d8cff;\n"
"                color: white;\n"
"                font-size: 13px;\n"
"                font-weight: 600;\n"
"                }\n"
"\n"
"                QPushButton:hover {\n"
"                background-color: #1f7ae6;\n"
"                }\n"
"            ")
        self.rowLayout = QHBoxLayout(StudentFeeRow)
        self.rowLayout.setSpacing(12)
        self.rowLayout.setObjectName(u"rowLayout")
        self.rowLayout.setContentsMargins(12, 8, 12, 8)
        self.label_sno = QLabel(StudentFeeRow)
        self.label_sno.setObjectName(u"label_sno")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_sno.sizePolicy().hasHeightForWidth())
        self.label_sno.setSizePolicy(sizePolicy)
        self.label_sno.setMinimumSize(QSize(60, 0))

        self.rowLayout.addWidget(self.label_sno)

        self.label_studentName = QLabel(StudentFeeRow)
        self.label_studentName.setObjectName(u"label_studentName")
        self.label_studentName.setMinimumSize(QSize(220, 0))
        self.label_studentName.setStyleSheet(u"font-weight: 600; font-size: 13px; color: #111;")

        self.rowLayout.addWidget(self.label_studentName)

        self.label_totalFee = QLabel(StudentFeeRow)
        self.label_totalFee.setObjectName(u"label_totalFee")
        self.label_totalFee.setMinimumSize(QSize(90, 0))
        self.label_totalFee.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.rowLayout.addWidget(self.label_totalFee)

        self.label_paidFee = QLabel(StudentFeeRow)
        self.label_paidFee.setObjectName(u"label_paidFee")
        self.label_paidFee.setMinimumSize(QSize(90, 0))
        self.label_paidFee.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.rowLayout.addWidget(self.label_paidFee)

        self.label_pendingFee = QLabel(StudentFeeRow)
        self.label_pendingFee.setObjectName(u"label_pendingFee")
        self.label_pendingFee.setMinimumSize(QSize(90, 0))
        self.label_pendingFee.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.rowLayout.addWidget(self.label_pendingFee)

        self.widget_2 = QWidget(StudentFeeRow)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_status = QLabel(self.widget_2)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setMinimumSize(QSize(90, 28))
        self.label_status.setMaximumSize(QSize(120, 28))
        self.label_status.setStyleSheet(u"\n"
"                            QLabel {\n"
"                            background-color: rgba(218, 55, 0, 40);\n"
"                            color: rgb(255, 37, 41);\n"
"                            border-radius: 5px;\n"
"                            padding: 4px 10px;\n"
"                            font-size: 12px;\n"
"                            font-weight: 600;\n"
"                            }\n"
"                        ")
        self.label_status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_status)


        self.rowLayout.addWidget(self.widget_2)

        self.widget = QWidget(StudentFeeRow)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_recordPayment = QPushButton(self.widget)
        self.btn_recordPayment.setObjectName(u"btn_recordPayment")
        self.btn_recordPayment.setMinimumSize(QSize(130, 30))
        self.btn_recordPayment.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_recordPayment)


        self.rowLayout.addWidget(self.widget)


        self.retranslateUi(StudentFeeRow)

        QMetaObject.connectSlotsByName(StudentFeeRow)
    # setupUi

    def retranslateUi(self, StudentFeeRow):
        self.label_sno.setText(QCoreApplication.translate("StudentFeeRow", u"1", None))
        self.label_studentName.setText(QCoreApplication.translate("StudentFeeRow", u"Student Name", None))
        self.label_totalFee.setText(QCoreApplication.translate("StudentFeeRow", u"\u20b90", None))
        self.label_paidFee.setText(QCoreApplication.translate("StudentFeeRow", u"\u20b90", None))
        self.label_pendingFee.setText(QCoreApplication.translate("StudentFeeRow", u"\u20b90", None))
        self.label_status.setText(QCoreApplication.translate("StudentFeeRow", u"Unpaid", None))
        self.btn_recordPayment.setText(QCoreApplication.translate("StudentFeeRow", u"Record Payment", None))
        pass
    # retranslateUi

