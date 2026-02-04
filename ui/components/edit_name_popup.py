from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtGui import (QCursor)
from PySide6.QtWidgets import (QFrame, QHBoxLayout,
                               QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget)


class Ui_EditNamePopup(object):
    def setupUi(self, EditNamePopup):
        if not EditNamePopup.objectName():
            EditNamePopup.setObjectName(u"EditNamePopup")
        EditNamePopup.resize(420, 260)
        EditNamePopup.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(EditNamePopup)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.backgroundFrame = QFrame(EditNamePopup)
        self.backgroundFrame.setObjectName(u"backgroundFrame")
        self.backgroundFrame.setStyleSheet(u"#backgroundFrame {\n"
                                           "    background-color: white;\n"
                                           "}\n"
                                           "\n"
                                           "QLabel {\n"
                                           "    color: #333;\n"
                                           "    font-family: \"Segoe UI\";\n"
                                           "    font-size: 20px;\n"
                                           "    font-weight: bold;\n"
                                           "    border: none;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton {\n"
                                           "    height: 35px;\n"
                                           "    padding: 0 16px;\n"
                                           "    background-color: #3388FF;\n"
                                           "    color: white;\n"
                                           "    font-size: 14px;\n"
                                           "    font-weight: 600;\n"
                                           "    border: none;\n"
                                           "    border-radius: 5px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: #0055FF;\n"
                                           "}")
        self.verticalLayout_2 = QVBoxLayout(self.backgroundFrame)
        self.verticalLayout_2.setSpacing(16)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(18, 18, 18, 18)
        self.title_label = QLabel(self.backgroundFrame)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.title_label)

        self.form_container = QWidget(self.backgroundFrame)
        self.form_container.setObjectName(u"form_container")
        self.form_container.setStyleSheet(u"QLabel{color : rgb(0,0,0);font: 600 8pt \"Segoe UI\";}\n"
                                          "QLineEdit {\n"
                                          "    height: 20px;\n"
                                          "    padding: 8px 10px;\n"
                                          "    font-size: 14px;\n"
                                          "    color: #111;\n"
                                          "    border: 1px solid rgb(99, 99, 99);\n"
                                          "    background: #fff;\n"
                                          "    border-radius: 4px;\n"
                                          "}\n"
                                          "QLineEdit:focus {\n"
                                          "    border: 1.5px solid #3388FF;\n"
                                          "}")
        self.verticalLayout_3 = QVBoxLayout(self.form_container)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.field_label = QLabel(self.form_container)
        self.field_label.setObjectName(u"field_label")

        self.verticalLayout_3.addWidget(self.field_label)

        self.name_input = QLineEdit(self.form_container)
        self.name_input.setObjectName(u"name_input")

        self.verticalLayout_3.addWidget(self.name_input)

        self.error_label = QLabel(self.form_container)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setStyleSheet(u"color: rgb(255, 82, 52); font: 600 8pt \"Segoe UI\";")
        self.error_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_3.addWidget(self.error_label)

        self.verticalLayout_2.addWidget(self.form_container)

        self.buttons_container = QWidget(self.backgroundFrame)
        self.buttons_container.setObjectName(u"buttons_container")
        self.horizontalLayout = QHBoxLayout(self.buttons_container)
        self.horizontalLayout.setSpacing(18)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_close = QPushButton(self.buttons_container)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_close.setStyleSheet(u"#btn_close{\n"
                                     "    background-color: rgb(255, 255, 255);\n"
                                     "    color: #333;\n"
                                     "    border: 1px solid #333;\n"
                                     "    border-radius: 5px;\n"
                                     "}\n"
                                     "\n"
                                     "#btn_close:hover{\n"
                                     "    background-color: rgba(51, 51, 51, 30);\n"
                                     "}\n"
                                     "\n"
                                     "#btn_close:pressed{\n"
                                     "    background-color: rgba(51, 51, 51, 80);\n"
                                     "}")

        self.horizontalLayout.addWidget(self.btn_close)

        self.btn_save = QPushButton(self.buttons_container)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_save)

        self.verticalLayout_2.addWidget(self.buttons_container)

        self.verticalLayout.addWidget(self.backgroundFrame)

        self.retranslateUi(EditNamePopup)

        QMetaObject.connectSlotsByName(EditNamePopup)

    # setupUi

    def retranslateUi(self, EditNamePopup):
        EditNamePopup.setWindowTitle(QCoreApplication.translate("EditNamePopup", u"Edit", None))
        self.title_label.setText(QCoreApplication.translate("EditNamePopup", u"Edit", None))
        self.field_label.setText(QCoreApplication.translate("EditNamePopup", u"Name", None))
        self.error_label.setText("")
        self.btn_close.setText(QCoreApplication.translate("EditNamePopup", u"Close", None))
        self.btn_save.setText(QCoreApplication.translate("EditNamePopup", u"Save", None))
    # retranslateUi
