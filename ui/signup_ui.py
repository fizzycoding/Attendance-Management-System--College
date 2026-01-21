# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signup.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtGui import (QCursor,
                           QFont)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel,
                               QLineEdit, QPushButton, QRadioButton, QSizePolicy,
                               QVBoxLayout, QWidget)


class Ui_signup_form_main_window(object):
    def setupUi(self, signup_form_main_window):
        if not signup_form_main_window.objectName():
            signup_form_main_window.setObjectName(u"signup_form_main_window")
        signup_form_main_window.resize(850, 580)
        signup_form_main_window.setStyleSheet(u"\n"
                                              "                #signup_form_main_window {\n"
                                              "                background: white;\n"
                                              "                }\n"
                                              "            ")
        self.mainLayout = QHBoxLayout(signup_form_main_window)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.leftFrame = QFrame(signup_form_main_window)
        self.leftFrame.setObjectName(u"leftFrame")
        self.leftFrame.setStyleSheet(u"\n"
                                     "                            #leftFrame {\n"
                                     "                            background: white;\n"
                                     "                            }\n"
                                     "                        ")
        self.leftFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.leftFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formContainer = QWidget(self.leftFrame)
        self.formContainer.setObjectName(u"formContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formContainer.sizePolicy().hasHeightForWidth())
        self.formContainer.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.formContainer)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, -1, 20, -1)
        self.headerWidget = QWidget(self.formContainer)
        self.headerWidget.setObjectName(u"headerWidget")
        sizePolicy.setHeightForWidth(self.headerWidget.sizePolicy().hasHeightForWidth())
        self.headerWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.headerWidget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.signupLabel = QLabel(self.headerWidget)
        self.signupLabel.setObjectName(u"signupLabel")
        self.signupLabel.setStyleSheet(u"\n"
                                       "                                                                #signupLabel {\n"
                                       "                                                                font: 700 20pt \"Arial\";\n"
                                       "                                                                color: black;\n"
                                       "                                                                }\n"
                                       "                                                            ")
        self.signupLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.signupLabel)

        self.signupSloganLabel = QLabel(self.headerWidget)
        self.signupSloganLabel.setObjectName(u"signupSloganLabel")
        self.signupSloganLabel.setStyleSheet(u"\n"
                                             "                                                                #signupSloganLabel {\n"
                                             "                                                                font-size: 12pt;\n"
                                             "                                                                color: #555;\n"
                                             "                                                                }\n"
                                             "                                                            ")
        self.signupSloganLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.signupSloganLabel.setWordWrap(True)

        self.verticalLayout.addWidget(self.signupSloganLabel)

        self.verticalLayout_4.addWidget(self.headerWidget)

        self.nameWidget = QWidget(self.formContainer)
        self.nameWidget.setObjectName(u"nameWidget")
        sizePolicy.setHeightForWidth(self.nameWidget.sizePolicy().hasHeightForWidth())
        self.nameWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_name = QVBoxLayout(self.nameWidget)
        self.verticalLayout_name.setSpacing(5)
        self.verticalLayout_name.setObjectName(u"verticalLayout_name")
        self.verticalLayout_name.setContentsMargins(0, 0, 0, 0)
        self.nameLabel = QLabel(self.nameWidget)
        self.nameLabel.setObjectName(u"nameLabel")
        sizePolicy.setHeightForWidth(self.nameLabel.sizePolicy().hasHeightForWidth())
        self.nameLabel.setSizePolicy(sizePolicy)
        self.nameLabel.setStyleSheet(u"#nameLabel{\n"
                                     "                                                                color : rgb(0,0,0);\n"
                                     "                                                                font: 600 8pt \"Segoe UI\";\n"
                                     "                                                                }\n"
                                     "                                                            ")

        self.verticalLayout_name.addWidget(self.nameLabel)

        self.nameInputBox = QLineEdit(self.nameWidget)
        self.nameInputBox.setObjectName(u"nameInputBox")
        sizePolicy.setHeightForWidth(self.nameInputBox.sizePolicy().hasHeightForWidth())
        self.nameInputBox.setSizePolicy(sizePolicy)
        self.nameInputBox.setStyleSheet(u"#nameInputBox {\n"
                                        "                                                                height: 20px;\n"
                                        "                                                                padding: 8px 10px;\n"
                                        "                                                                font-size: 14px;\n"
                                        "                                                                color: #111;\n"
                                        "                                                                border: 1px solid rgb(99, 99, 99);\n"
                                        "                                                                background: #fff;\n"
                                        "                                                                border-radius: 4px;\n"
                                        "                                                                }\n"
                                        "                                                                #nameInputBox:focus {\n"
                                        "                                                                border: 1.5px solid #2ab79d;\n"
                                        "                                                                }\n"
                                        "                                                            ")

        self.verticalLayout_name.addWidget(self.nameInputBox)

        self.verticalLayout_4.addWidget(self.nameWidget)

        self.userWidget = QWidget(self.formContainer)
        self.userWidget.setObjectName(u"userWidget")
        sizePolicy.setHeightForWidth(self.userWidget.sizePolicy().hasHeightForWidth())
        self.userWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_user = QVBoxLayout(self.userWidget)
        self.verticalLayout_user.setSpacing(5)
        self.verticalLayout_user.setObjectName(u"verticalLayout_user")
        self.verticalLayout_user.setContentsMargins(0, 0, 0, 0)
        self.inputLabel = QLabel(self.userWidget)
        self.inputLabel.setObjectName(u"inputLabel")
        sizePolicy.setHeightForWidth(self.inputLabel.sizePolicy().hasHeightForWidth())
        self.inputLabel.setSizePolicy(sizePolicy)
        self.inputLabel.setStyleSheet(u"#inputLabel{\n"
                                      "                                                                color : rgb(0,0,0);\n"
                                      "                                                                font: 600 8pt \"Segoe UI\";\n"
                                      "                                                                }\n"
                                      "                                                            ")

        self.verticalLayout_user.addWidget(self.inputLabel)

        self.usernameInputBox = QLineEdit(self.userWidget)
        self.usernameInputBox.setObjectName(u"usernameInputBox")
        self.usernameInputBox.setStyleSheet(u"#usernameInputBox {\n"
                                            "                                                                height: 20px;\n"
                                            "                                                                padding: 8px 10px;\n"
                                            "                                                                font-size: 14px;\n"
                                            "                                                                color: #111;\n"
                                            "                                                                border: 1px solid rgb(99, 99, 99);\n"
                                            "                                                                background: #fff;\n"
                                            "                                                                border-radius: 4px;\n"
                                            "                                                                }\n"
                                            "                                                                #usernameInputBox:focus {\n"
                                            "                                                                border: 1.5px solid #2ab79d;\n"
                                            "                                                                }\n"
                                            "                                                          "
                                            "  ")

        self.verticalLayout_user.addWidget(self.usernameInputBox)

        self.verticalLayout_4.addWidget(self.userWidget)

        self.passWidget = QWidget(self.formContainer)
        self.passWidget.setObjectName(u"passWidget")
        sizePolicy.setHeightForWidth(self.passWidget.sizePolicy().hasHeightForWidth())
        self.passWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_pass = QVBoxLayout(self.passWidget)
        self.verticalLayout_pass.setSpacing(5)
        self.verticalLayout_pass.setObjectName(u"verticalLayout_pass")
        self.verticalLayout_pass.setContentsMargins(0, 0, 0, 0)
        self.passLabel = QLabel(self.passWidget)
        self.passLabel.setObjectName(u"passLabel")
        sizePolicy.setHeightForWidth(self.passLabel.sizePolicy().hasHeightForWidth())
        self.passLabel.setSizePolicy(sizePolicy)
        self.passLabel.setStyleSheet(u"#passLabel{\n"
                                     "                                                                color : rgb(0,0,0);\n"
                                     "                                                                font: 600 8pt \"Segoe UI\";\n"
                                     "                                                                }\n"
                                     "                                                            ")

        self.verticalLayout_pass.addWidget(self.passLabel)

        self.passwordInputBox = QLineEdit(self.passWidget)
        self.passwordInputBox.setObjectName(u"passwordInputBox")
        self.passwordInputBox.setStyleSheet(u"#passwordInputBox {\n"
                                            "                                                                height: 20px;\n"
                                            "                                                                padding: 8px 10px;\n"
                                            "                                                                font-size: 14px;\n"
                                            "                                                                color: #111;\n"
                                            "                                                                border: 1px solid rgb(99, 99, 99);\n"
                                            "                                                                background: #fff;\n"
                                            "                                                                border-radius: 4px;\n"
                                            "                                                                }\n"
                                            "                                                                #passwordInputBox:focus {\n"
                                            "                                                                border: 1.5px solid #2ab79d;\n"
                                            "                                                                }\n"
                                            "                                                          "
                                            "  ")
        self.passwordInputBox.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_pass.addWidget(self.passwordInputBox)

        self.verticalLayout_4.addWidget(self.passWidget)

        self.roleWidget = QWidget(self.formContainer)
        self.roleWidget.setObjectName(u"roleWidget")
        sizePolicy.setHeightForWidth(self.roleWidget.sizePolicy().hasHeightForWidth())
        self.roleWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_role = QVBoxLayout(self.roleWidget)
        self.verticalLayout_role.setSpacing(10)
        self.verticalLayout_role.setObjectName(u"verticalLayout_role")
        self.verticalLayout_role.setContentsMargins(0, 0, 0, 0)
        self.roleLabel = QLabel(self.roleWidget)
        self.roleLabel.setObjectName(u"roleLabel")
        sizePolicy.setHeightForWidth(self.roleLabel.sizePolicy().hasHeightForWidth())
        self.roleLabel.setSizePolicy(sizePolicy)
        self.roleLabel.setStyleSheet(u"#roleLabel{\n"
                                     "                                                                color : rgb(0,0,0);\n"
                                     "                                                                font: 600 8pt \"Segoe UI\";\n"
                                     "                                                                }\n"
                                     "                                                            ")

        self.verticalLayout_role.addWidget(self.roleLabel)

        self.radioContainer = QWidget(self.roleWidget)
        self.radioContainer.setObjectName(u"radioContainer")
        sizePolicy.setHeightForWidth(self.radioContainer.sizePolicy().hasHeightForWidth())
        self.radioContainer.setSizePolicy(sizePolicy)
        self.radioContainer.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout_role = QHBoxLayout(self.radioContainer)
        self.horizontalLayout_role.setObjectName(u"horizontalLayout_role")
        self.horizontalLayout_role.setContentsMargins(0, 0, -1, -1)
        self.studentRadioButton = QRadioButton(self.radioContainer)
        self.studentRadioButton.setObjectName(u"studentRadioButton")
        sizePolicy.setHeightForWidth(self.studentRadioButton.sizePolicy().hasHeightForWidth())
        self.studentRadioButton.setSizePolicy(sizePolicy)
        self.studentRadioButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.studentRadioButton.setStyleSheet(u"\n"
                                              "                                                                            QRadioButton {\n"
                                              "                                                                            font-size: 14px;\n"
                                              "                                                                            color: #333;\n"
                                              "                                                                            }\n"
                                              "                                                                            QRadioButton::indicator {\n"
                                              "                                                                            width: 14px;\n"
                                              "                                                                            height: 14px;\n"
                                              "                                                                            border-radius: 7px;\n"
                                              "                                                                            border: 1px solid #999;\n"
                                              "                                                                            }\n"
                                              "                                                                          "
                                              "  QRadioButton::indicator:checked {\n"
                                              "                                                                            background-color: #159079;\n"
                                              "                                                                            border: 1px solid #067d68;\n"
                                              "                                                                            }\n"
                                              "                                                                        ")
        self.studentRadioButton.setChecked(True)

        self.horizontalLayout_role.addWidget(self.studentRadioButton)

        self.teacherRadioButton = QRadioButton(self.radioContainer)
        self.teacherRadioButton.setObjectName(u"teacherRadioButton")
        self.teacherRadioButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.teacherRadioButton.setStyleSheet(u"\n"
                                              "                                                                            QRadioButton {\n"
                                              "                                                                            font-size: 14px;\n"
                                              "                                                                            color: #333;\n"
                                              "                                                                            }\n"
                                              "                                                                            QRadioButton::indicator {\n"
                                              "                                                                            width: 14px;\n"
                                              "                                                                            height: 14px;\n"
                                              "                                                                            border-radius: 7px;\n"
                                              "                                                                            border: 1px solid #999;\n"
                                              "                                                                            }\n"
                                              "                                                                          "
                                              "  QRadioButton::indicator:checked {\n"
                                              "                                                                            background-color: #159079;\n"
                                              "                                                                            border: 1px solid #067d68;\n"
                                              "                                                                            }\n"
                                              "                                                                        ")

        self.horizontalLayout_role.addWidget(self.teacherRadioButton)

        self.verticalLayout_role.addWidget(self.radioContainer)

        self.verticalLayout_4.addWidget(self.roleWidget)

        self.erroLabel = QLabel(self.formContainer)
        self.erroLabel.setObjectName(u"erroLabel")
        sizePolicy.setHeightForWidth(self.erroLabel.sizePolicy().hasHeightForWidth())
        self.erroLabel.setSizePolicy(sizePolicy)
        self.erroLabel.setStyleSheet(u"#erroLabel{\n"
                                     "                                                    color : rgb(255,0,0);\n"
                                     "                                                    font: 600 8pt \"Segoe UI\";\n"
                                     "                                                    }\n"
                                     "                                                ")

        self.verticalLayout_4.addWidget(self.erroLabel)

        self.registerButton = QPushButton(self.formContainer)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.registerButton.setStyleSheet(u"#registerButton {\n"
                                          "                                                    height: 44px;\n"
                                          "                                                    padding: 0 16px;\n"
                                          "                                                    background-color: #2ab79d;\n"
                                          "                                                    color: white;\n"
                                          "                                                    font-size: 14px;\n"
                                          "                                                    font-weight: 600;\n"
                                          "                                                    border: none;\n"
                                          "                                                    border-radius: 8px;\n"
                                          "                                                    }\n"
                                          "\n"
                                          "                                                    #registerButton:hover {\n"
                                          "                                                    background-color: #159079;\n"
                                          "                                                    }\n"
                                          "                                                ")

        self.verticalLayout_4.addWidget(self.registerButton)

        self.verticalLayout_2.addWidget(self.formContainer)

        self.mainLayout.addWidget(self.leftFrame)

        self.rightFrame = QFrame(signup_form_main_window)
        self.rightFrame.setObjectName(u"rightFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.rightFrame.sizePolicy().hasHeightForWidth())
        self.rightFrame.setSizePolicy(sizePolicy1)
        self.rightFrame.setStyleSheet(u"\n"
                                      "                            #rightFrame {\n"
                                      "                            background: qlineargradient(\n"
                                      "                            x1:0, y1:0,\n"
                                      "                            x2:0, y2:1,\n"
                                      "                            stop:0 #50d5b7,\n"
                                      "                            stop:1 #067d68\n"
                                      "                            );\n"
                                      "                            }\n"
                                      "                        ")
        self.verticalLayout_5 = QVBoxLayout(self.rightFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.contentContainer = QWidget(self.rightFrame)
        self.contentContainer.setObjectName(u"contentContainer")
        sizePolicy.setHeightForWidth(self.contentContainer.sizePolicy().hasHeightForWidth())
        self.contentContainer.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.contentContainer)
        self.verticalLayout_6.setSpacing(30)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(50, 30, 50, -1)
        self.textWidget = QWidget(self.contentContainer)
        self.textWidget.setObjectName(u"textWidget")
        sizePolicy.setHeightForWidth(self.textWidget.sizePolicy().hasHeightForWidth())
        self.textWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QVBoxLayout(self.textWidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.welcomeBackLabel = QLabel(self.textWidget)
        self.welcomeBackLabel.setObjectName(u"welcomeBackLabel")
        sizePolicy.setHeightForWidth(self.welcomeBackLabel.sizePolicy().hasHeightForWidth())
        self.welcomeBackLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.welcomeBackLabel.setFont(font)
        self.welcomeBackLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.welcomeBackLabel)

        self.subTextLabel = QLabel(self.textWidget)
        self.subTextLabel.setObjectName(u"subTextLabel")
        sizePolicy.setHeightForWidth(self.subTextLabel.sizePolicy().hasHeightForWidth())
        self.subTextLabel.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(11)
        self.subTextLabel.setFont(font1)
        self.subTextLabel.setStyleSheet(u"#subTextLabel{\n"
                                        "                                                                color: rgba(255, 255, 255, 192)}\n"
                                        "                                                            ")
        self.subTextLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.subTextLabel.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.subTextLabel)

        self.verticalLayout_6.addWidget(self.textWidget)

        self.switchLoginButton = QPushButton(self.contentContainer)
        self.switchLoginButton.setObjectName(u"switchLoginButton")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(False)
        self.switchLoginButton.setFont(font2)
        self.switchLoginButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.switchLoginButton.setStyleSheet(u"#switchLoginButton{\n"
                                             "                                                    border-radius: 18px;\n"
                                             "                                                    border:1px solid rgba(255, 255, 255, 150);\n"
                                             "                                                    padding: 7px 0;\n"
                                             "                                                    color: white;\n"
                                             "                                                    }\n"
                                             "\n"
                                             "                                                    #switchLoginButton:hover{\n"
                                             "                                                    border:1px solid #fff;\n"
                                             "                                                    background: rgba(255, 255, 255, 30);\n"
                                             "                                                    }\n"
                                             "                                                ")

        self.verticalLayout_6.addWidget(self.switchLoginButton)

        self.verticalLayout_5.addWidget(self.contentContainer)

        self.mainLayout.addWidget(self.rightFrame)

        self.mainLayout.setStretch(0, 1)
        self.mainLayout.setStretch(1, 1)

        self.retranslateUi(signup_form_main_window)

        QMetaObject.connectSlotsByName(signup_form_main_window)

    # setupUi

    def retranslateUi(self, signup_form_main_window):
        signup_form_main_window.setWindowTitle(QCoreApplication.translate("signup_form_main_window", u"Sign Up", None))
        self.signupLabel.setText(QCoreApplication.translate("signup_form_main_window", u"Create Account", None))
        self.signupSloganLabel.setText(
            QCoreApplication.translate("signup_form_main_window", u"Fill in your details to join us", None))
        self.nameLabel.setText(QCoreApplication.translate("signup_form_main_window", u"Full Name", None))
        self.inputLabel.setText(QCoreApplication.translate("signup_form_main_window", u"Username", None))
        self.passLabel.setText(QCoreApplication.translate("signup_form_main_window", u"Password", None))
        self.roleLabel.setText(QCoreApplication.translate("signup_form_main_window", u"Select Role", None))
        self.studentRadioButton.setText(QCoreApplication.translate("signup_form_main_window", u"Student", None))
        self.teacherRadioButton.setText(QCoreApplication.translate("signup_form_main_window", u"Teacher", None))
        self.erroLabel.setText("")
        self.registerButton.setText(QCoreApplication.translate("signup_form_main_window", u"Sign Up", None))
        self.welcomeBackLabel.setStyleSheet(
            QCoreApplication.translate("signup_form_main_window", u"color: white;", None))
        self.welcomeBackLabel.setText(QCoreApplication.translate("signup_form_main_window", u"Welcome Back!", None))
        self.subTextLabel.setText(QCoreApplication.translate("signup_form_main_window",
                                                             u"Already have an account? Login with your personal info.\n""                                                            ",
                                                             None))
        self.switchLoginButton.setText(QCoreApplication.translate("signup_form_main_window", u"Log In", None))
    # retranslateUi
