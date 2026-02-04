from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QSizePolicy)


class Ui_reportStudentNameRow(object):
    def setupUi(self, reportStudentNameRow):
        if not reportStudentNameRow.objectName():
            reportStudentNameRow.setObjectName(u"reportStudentNameRow")
        reportStudentNameRow.resize(569, 50)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(reportStudentNameRow.sizePolicy().hasHeightForWidth())
        reportStudentNameRow.setSizePolicy(sizePolicy)
        reportStudentNameRow.setMinimumSize(QSize(0, 50))
        reportStudentNameRow.setMaximumSize(QSize(16777215, 50))
        reportStudentNameRow.setStyleSheet(u"#reportStudentNameRow{border-top: 1px solid;\n"
                                           "border-top-color: rgb(200,200,200);}\n"
                                           "#reportStudentNameRow:hover{\n"
                                           "background-color: rgba(51, 143, 255,10)}\n"
                                           "QLabel{background-color:transparent;\n"
                                           "\n"
                                           "font: 10pt \"Segoe UI\";}")
        self.horizontalLayout = QHBoxLayout(reportStudentNameRow)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, 0, 0, 0)
        self.sNumber = QLabel(reportStudentNameRow)
        self.sNumber.setObjectName(u"sNumber")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(55)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sNumber.sizePolicy().hasHeightForWidth())
        self.sNumber.setSizePolicy(sizePolicy1)
        self.sNumber.setMinimumSize(QSize(60, 0))
        self.sNumber.setStyleSheet(u"color: #383838; font: 600 10pt \"Segoe UI\";")
        self.sNumber.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.sNumber)

        self.name = QLabel(reportStudentNameRow)
        self.name.setObjectName(u"name")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy2)
        self.name.setStyleSheet(u"color: rgb(43, 43, 43); font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.name)

        self.rate = QLabel(reportStudentNameRow)
        self.rate.setObjectName(u"rate")
        sizePolicy2.setHeightForWidth(self.rate.sizePolicy().hasHeightForWidth())
        self.rate.setSizePolicy(sizePolicy2)
        self.rate.setMaximumSize(QSize(75, 16777215))
        self.rate.setStyleSheet(u"color: rgb(28, 164, 255);\n"
                                "font: 700 12pt \"Segoe UI\";")
        self.rate.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.rate)

        self.retranslateUi(reportStudentNameRow)

        QMetaObject.connectSlotsByName(reportStudentNameRow)

    # setupUi

    def retranslateUi(self, reportStudentNameRow):
        reportStudentNameRow.setWindowTitle(QCoreApplication.translate("reportStudentNameRow", u"Form", None))
        self.sNumber.setText(QCoreApplication.translate("reportStudentNameRow", u"1", None))
        self.name.setText(QCoreApplication.translate("reportStudentNameRow", u"Rahul", None))
        self.rate.setText(QCoreApplication.translate("reportStudentNameRow", u"90%", None))
    # retranslateUi
