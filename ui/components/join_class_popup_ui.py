from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtGui import (QCursor)
from PySide6.QtWidgets import (QFrame, QHBoxLayout,
                               QLabel, QLineEdit, QPushButton, QSizePolicy,
                               QVBoxLayout, QWidget)


class Ui_JoinClassPopup(object):
    def setupUi(self, JoinClassPopup):
        if not JoinClassPopup.objectName():
            JoinClassPopup.setObjectName(u"JoinClassPopup")
        JoinClassPopup.resize(400, 250)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(JoinClassPopup.sizePolicy().hasHeightForWidth())
        JoinClassPopup.setSizePolicy(sizePolicy)
        JoinClassPopup.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(JoinClassPopup)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.backgroundFrame = QFrame(JoinClassPopup)
        self.backgroundFrame.setObjectName(u"backgroundFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.backgroundFrame.sizePolicy().hasHeightForWidth())
        self.backgroundFrame.setSizePolicy(sizePolicy1)
        self.backgroundFrame.setStyleSheet(u"#backgroundFrame {\n"
                                           "    background-color: white;\n"
                                           "}\n"
                                           "QLabel {\n"
                                           "    color: #333;\n"
                                           "    font-family: \"Segoe UI\";\n"
                                           "    font-size: 20px;\n"
                                           "    font-weight: bold;\n"
                                           "    border: none; }\n"
                                           "\n"
                                           "QPushButton {\n"
                                           "height: 35px;\n"
                                           "padding: 0 16px;\n"
                                           "background-color: #3388FF;\n"
                                           "color: white;\n"
                                           "font-size: 14px;\n"
                                           "font-weight: 600;\n"
                                           "border: none;\n"
                                           "border-radius: 5px;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "background-color: #0055FF;\n"
                                           "}\n"
                                           "                                                ")
        self.backgroundFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.backgroundFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.backgroundFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.backgroundFrame)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.widget = QWidget(self.backgroundFrame)
        self.widget.setObjectName(u"widget")
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setStyleSheet(u"QLabel{color : rgb(0,0,0);font: 600 8pt \"Segoe UI\";}\n"
                                  "QLineEdit {\n"
                                  "                                                                height: 20px;\n"
                                  "                                                                padding: 8px 10px;\n"
                                  "                                                                font-size: 14px;\n"
                                  "                                                                color: #111;\n"
                                  "                                                                border: 1px solid rgb(99, 99, 99);\n"
                                  "                                                                background: #fff;\n"
                                  "                                                                border-radius: 4px;\n"
                                  "                                                                }\n"
                                  "QLineEdit:focus {\n"
                                  "border: 1.5px solid #3388FF;}")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.label_2)

        self.class_name_input = QLineEdit(self.widget)
        self.class_name_input.setObjectName(u"class_name_input")
        self.class_name_input.setMaxLength(6)

        self.verticalLayout_3.addWidget(self.class_name_input)

        self.verticalLayout_2.addWidget(self.widget)

        self.widget_2 = QWidget(self.backgroundFrame)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(18)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_close = QPushButton(self.widget_2)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_close.setStyleSheet(u"#btn_close{background-color: rgb(255, 255, 255);\n"
                                     "color: #333;\n"
                                     "border: 1px solid #333;\n"
                                     "border-radius: 5px\n"
                                     "}\n"
                                     "\n"
                                     "#btn_close:hover{\n"
                                     "	background-color: rgba(51, 51, 51, 30);\n"
                                     "}\n"
                                     "\n"
                                     "#btn_close:pressed{\n"
                                     "	background-color: rgba(51, 51, 51, 80);\n"
                                     "}\n"
                                     "")

        self.horizontalLayout_2.addWidget(self.btn_close)

        self.btn_create = QPushButton(self.widget_2)
        self.btn_create.setObjectName(u"btn_create")
        self.btn_create.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btn_create)

        self.verticalLayout_2.addWidget(self.widget_2)

        self.verticalLayout.addWidget(self.backgroundFrame)

        self.retranslateUi(JoinClassPopup)

        QMetaObject.connectSlotsByName(JoinClassPopup)

    # setupUi

    def retranslateUi(self, JoinClassPopup):
        JoinClassPopup.setWindowTitle(QCoreApplication.translate("JoinClassPopup", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("JoinClassPopup", u"Join Class", None))
        self.label_2.setText(QCoreApplication.translate("JoinClassPopup", u"Enter invite Code", None))
        self.btn_close.setText(QCoreApplication.translate("JoinClassPopup", u"Close", None))
        self.btn_create.setText(QCoreApplication.translate("JoinClassPopup", u"Join", None))
    # retranslateUi
