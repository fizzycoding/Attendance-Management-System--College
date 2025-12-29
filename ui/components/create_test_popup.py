from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtGui import (QCursor)
from PySide6.QtWidgets import (QAbstractSpinBox, QDateEdit, QFrame, QHBoxLayout, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
                               QVBoxLayout, QWidget)


class Ui_CreateTestPopup(object):
    def setupUi(self, CreateTestPopup):
        if not CreateTestPopup.objectName():
            CreateTestPopup.setObjectName(u"CreateTestPopup")
        CreateTestPopup.resize(450, 450)
        CreateTestPopup.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(CreateTestPopup)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.backgroundFrame = QFrame(CreateTestPopup)
        self.backgroundFrame.setObjectName(u"backgroundFrame")
        self.backgroundFrame.setStyleSheet(u"#backgroundFrame {\n"
                                           "    background-color: white;\n"
                                           "}\n"
                                           "QLabel {\n"
                                           "    color: #333;\n"
                                           "    font-family: \"Segoe UI\";\n"
                                           "    font-size: 14px;\n"
                                           "    font-weight: 600;\n"
                                           "    border: none; \n"
                                           "}\n"
                                           "\n"
                                           "/* Green Button Style */\n"
                                           "QPushButton {\n"
                                           "    height: 35px;\n"
                                           "    padding: 0 16px;\n"
                                           "    background-color: #2ab79d;\n"
                                           "    color: white;\n"
                                           "    font-family: \"Segoe UI\";\n"
                                           "    font-size: 14px;\n"
                                           "    font-weight: 600;\n"
                                           "    border: none;\n"
                                           "    border-radius: 5px;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: #159079;\n"
                                           "}\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color: #044d40;\n"
                                           "}\n"
                                           "")
        self.backgroundFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.backgroundFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.backgroundFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_title = QLabel(self.backgroundFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setStyleSheet(u"font-size: 20px; font-weight: bold; margin-bottom: 10px;")
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_title)

        self.widget_inputs = QWidget(self.backgroundFrame)
        self.widget_inputs.setObjectName(u"widget_inputs")
        self.widget_inputs.setStyleSheet(u"\n"
                                         "/* General Input Style */\n"
                                         "QLineEdit, QSpinBox, QDateEdit {\n"
                                         "    height: 35px;\n"
                                         "    padding: 0 10px;\n"
                                         "    font-family: \"Segoe UI\";\n"
                                         "    font-size: 14px;\n"
                                         "    color: #111;\n"
                                         "    border: 1px solid rgb(99, 99, 99);\n"
                                         "    background: #fff;\n"
                                         "    border-radius: 4px;\n"
                                         "}\n"
                                         "QLineEdit:focus, QSpinBox:focus, QDateEdit:focus {\n"
                                         "    border: 1.5px solid #2ab79d;\n"
                                         "}\n"
                                         "\n"
                                         "/* --- FIX: Calendar Colors --- */\n"
                                         "QCalendarWidget QWidget {\n"
                                         "    background-color: white; \n"
                                         "    color: black;\n"
                                         "}\n"
                                         "QCalendarWidget QAbstractItemView:enabled {\n"
                                         "    color: black; \n"
                                         "    background-color: white;\n"
                                         "    selection-background-color: #2ab79d; \n"
                                         "    selection-color: white;\n"
                                         "}\n"
                                         "QCalendarWidget QToolButton {\n"
                                         "    color: black;\n"
                                         "    icon-size: 25px;\n"
                                         "    background-color: white;\n"
                                         "}\n"
                                         "QCalendarWidget QSpinBox {\n"
                                         "    background-color: white;\n"
                                         "    color: black;\n"
                                         "}\n"
                                         "")
        self.verticalLayout_3 = QVBoxLayout(self.widget_inputs)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.layout_name = QVBoxLayout()
        self.layout_name.setSpacing(5)
        self.layout_name.setObjectName(u"layout_name")
        self.label_name = QLabel(self.widget_inputs)
        self.label_name.setObjectName(u"label_name")

        self.layout_name.addWidget(self.label_name)

        self.input_test_name = QLineEdit(self.widget_inputs)
        self.input_test_name.setObjectName(u"input_test_name")

        self.layout_name.addWidget(self.input_test_name)

        self.verticalLayout_3.addLayout(self.layout_name)

        self.horizontalLayout_marks = QHBoxLayout()
        self.horizontalLayout_marks.setSpacing(15)
        self.horizontalLayout_marks.setObjectName(u"horizontalLayout_marks")
        self.layout_max = QVBoxLayout()
        self.layout_max.setSpacing(5)
        self.layout_max.setObjectName(u"layout_max")
        self.label_max = QLabel(self.widget_inputs)
        self.label_max.setObjectName(u"label_max")

        self.layout_max.addWidget(self.label_max)

        self.input_max_marks = QSpinBox(self.widget_inputs)
        self.input_max_marks.setObjectName(u"input_max_marks")
        self.input_max_marks.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.input_max_marks.setMaximum(1000)
        self.input_max_marks.setValue(50)

        self.layout_max.addWidget(self.input_max_marks)

        self.horizontalLayout_marks.addLayout(self.layout_max)

        self.layout_pass = QVBoxLayout()
        self.layout_pass.setSpacing(5)
        self.layout_pass.setObjectName(u"layout_pass")
        self.label_pass = QLabel(self.widget_inputs)
        self.label_pass.setObjectName(u"label_pass")

        self.layout_pass.addWidget(self.label_pass)

        self.input_pass_marks = QSpinBox(self.widget_inputs)
        self.input_pass_marks.setObjectName(u"input_pass_marks")
        self.input_pass_marks.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.input_pass_marks.setMaximum(1000)
        self.input_pass_marks.setValue(17)

        self.layout_pass.addWidget(self.input_pass_marks)

        self.horizontalLayout_marks.addLayout(self.layout_pass)

        self.verticalLayout_3.addLayout(self.horizontalLayout_marks)

        self.layout_date = QVBoxLayout()
        self.layout_date.setSpacing(5)
        self.layout_date.setObjectName(u"layout_date")
        self.label_date = QLabel(self.widget_inputs)
        self.label_date.setObjectName(u"label_date")

        self.layout_date.addWidget(self.label_date)

        self.input_date = QDateEdit(self.widget_inputs)
        self.input_date.setObjectName(u"input_date")
        self.input_date.setCalendarPopup(True)

        self.layout_date.addWidget(self.input_date)

        self.verticalLayout_3.addLayout(self.layout_date)

        self.verticalLayout_2.addWidget(self.widget_inputs)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.widget_footer = QWidget(self.backgroundFrame)
        self.widget_footer.setObjectName(u"widget_footer")
        self.horizontalLayout_btns = QHBoxLayout(self.widget_footer)
        self.horizontalLayout_btns.setSpacing(15)
        self.horizontalLayout_btns.setObjectName(u"horizontalLayout_btns")
        self.btn_cancel = QPushButton(self.widget_footer)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cancel.setStyleSheet(u"\n"
                                      "#btn_cancel {\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "    color: #333;\n"
                                      "    border: 1px solid #333;\n"
                                      "}\n"
                                      "#btn_cancel:hover {\n"
                                      "    background-color: rgba(51, 51, 51, 30);\n"
                                      "}\n"
                                      "#btn_cancel:pressed {\n"
                                      "    background-color: rgba(51, 51, 51, 80);\n"
                                      "}\n"
                                      "")

        self.horizontalLayout_btns.addWidget(self.btn_cancel)

        self.btn_create = QPushButton(self.widget_footer)
        self.btn_create.setObjectName(u"btn_create")
        self.btn_create.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_btns.addWidget(self.btn_create)

        self.verticalLayout_2.addWidget(self.widget_footer)

        self.verticalLayout.addWidget(self.backgroundFrame)

        self.retranslateUi(CreateTestPopup)

        QMetaObject.connectSlotsByName(CreateTestPopup)

    # setupUi

    def retranslateUi(self, CreateTestPopup):
        CreateTestPopup.setWindowTitle(QCoreApplication.translate("CreateTestPopup", u"Create New Test", None))
        self.label_title.setText(QCoreApplication.translate("CreateTestPopup", u"Create New Test", None))
        self.label_name.setText(QCoreApplication.translate("CreateTestPopup", u"Test Name", None))
        self.input_test_name.setPlaceholderText(
            QCoreApplication.translate("CreateTestPopup", u"e.g. Unit Test 1", None))
        self.label_max.setText(QCoreApplication.translate("CreateTestPopup", u"Max Marks", None))
        self.label_pass.setText(QCoreApplication.translate("CreateTestPopup", u"Passing Marks", None))
        self.label_date.setText(QCoreApplication.translate("CreateTestPopup", u"Date", None))
        self.input_date.setDisplayFormat(QCoreApplication.translate("CreateTestPopup", u"dd-MMM-yyyy", None))
        self.btn_cancel.setText(QCoreApplication.translate("CreateTestPopup", u"Cancel", None))
        self.btn_create.setText(QCoreApplication.translate("CreateTestPopup", u"Create", None))
    # retranslateUi
