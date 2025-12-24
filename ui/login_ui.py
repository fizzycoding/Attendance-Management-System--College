# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_login_form_main_window(object):
    def setupUi(self, login_form_main_window):
        if not login_form_main_window.objectName():
            login_form_main_window.setObjectName(u"login_form_main_window")
        login_form_main_window.resize(850, 580)
        login_form_main_window.setStyleSheet(u"\n"
"                #login_form_main_window {\n"
"                background: white;\n"
"                }\n"
"            ")
        self.mainLayout = QHBoxLayout(login_form_main_window)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.leftFrame = QFrame(login_form_main_window)
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
        self.loginLabel = QLabel(self.headerWidget)
        self.loginLabel.setObjectName(u"loginLabel")
        sizePolicy.setHeightForWidth(self.loginLabel.sizePolicy().hasHeightForWidth())
        self.loginLabel.setSizePolicy(sizePolicy)
        self.loginLabel.setStyleSheet(u"\n"
"                                                                #loginLabel {\n"
"                                                                font: 700 20pt \"Arial\";\n"
"                                                                color: black;\n"
"                                                                }\n"
"                                                            ")
        self.loginLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.loginLabel)

        self.loginSloganLabel = QLabel(self.headerWidget)
        self.loginSloganLabel.setObjectName(u"loginSloganLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.loginSloganLabel.sizePolicy().hasHeightForWidth())
        self.loginSloganLabel.setSizePolicy(sizePolicy1)
        self.loginSloganLabel.setStyleSheet(u"\n"
"                                                                #loginSloganLabel {\n"
"                                                                font-size: 12pt;\n"
"                                                                color: #555;\n"
"                                                                }\n"
"                                                            ")
        self.loginSloganLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.loginSloganLabel.setWordWrap(True)

        self.verticalLayout.addWidget(self.loginSloganLabel)


        self.verticalLayout_4.addWidget(self.headerWidget)

        self.usernameWidget = QWidget(self.formContainer)
        self.usernameWidget.setObjectName(u"usernameWidget")
        sizePolicy.setHeightForWidth(self.usernameWidget.sizePolicy().hasHeightForWidth())
        self.usernameWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.usernameWidget)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.usernameLabel = QLabel(self.usernameWidget)
        self.usernameLabel.setObjectName(u"usernameLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.usernameLabel.sizePolicy().hasHeightForWidth())
        self.usernameLabel.setSizePolicy(sizePolicy2)
        self.usernameLabel.setStyleSheet(u"#usernameLabel{\n"
"                                                                color : rgb(0,0,0);\n"
"                                                                font: 600 8pt \"Segoe UI\";\n"
"                                                                }\n"
"                                                            ")

        self.verticalLayout_3.addWidget(self.usernameLabel)

        self.usernameInputBox = QLineEdit(self.usernameWidget)
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
"\n"
"                                                                #usernameInputBox:focus {\n"
"                                                                border: 1.5px solid #2ab79d;\n"
"                                                                }\n"
"                                                     "
                        "       ")

        self.verticalLayout_3.addWidget(self.usernameInputBox)


        self.verticalLayout_4.addWidget(self.usernameWidget)

        self.passwordWidget = QWidget(self.formContainer)
        self.passwordWidget.setObjectName(u"passwordWidget")
        sizePolicy.setHeightForWidth(self.passwordWidget.sizePolicy().hasHeightForWidth())
        self.passwordWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_pass = QVBoxLayout(self.passwordWidget)
        self.verticalLayout_pass.setSpacing(5)
        self.verticalLayout_pass.setObjectName(u"verticalLayout_pass")
        self.verticalLayout_pass.setContentsMargins(0, 0, 0, 0)
        self.passwordLabel = QLabel(self.passwordWidget)
        self.passwordLabel.setObjectName(u"passwordLabel")
        sizePolicy2.setHeightForWidth(self.passwordLabel.sizePolicy().hasHeightForWidth())
        self.passwordLabel.setSizePolicy(sizePolicy2)
        self.passwordLabel.setStyleSheet(u"#passwordLabel{\n"
"                                                                color : rgb(0,0,0);\n"
"                                                                font: 600 8pt \"Segoe UI\";\n"
"                                                                }\n"
"                                                            ")

        self.verticalLayout_pass.addWidget(self.passwordLabel)

        self.passwordInputBox = QLineEdit(self.passwordWidget)
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
"\n"
"                                                                #passwordInputBox:focus {\n"
"                                                                border: 1.5px solid #2ab79d;\n"
"                                                                }\n"
"                                                     "
                        "       ")
        self.passwordInputBox.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_pass.addWidget(self.passwordInputBox)


        self.verticalLayout_4.addWidget(self.passwordWidget)

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

        self.loginButton = QPushButton(self.formContainer)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.loginButton.setStyleSheet(u"#loginButton {\n"
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
"                                                    #loginButton:hover {\n"
"                                                    background-color: #159079;\n"
"                                                    }\n"
"                                                ")

        self.verticalLayout_4.addWidget(self.loginButton)


        self.verticalLayout_2.addWidget(self.formContainer)


        self.mainLayout.addWidget(self.leftFrame)

        self.rightFrame = QFrame(login_form_main_window)
        self.rightFrame.setObjectName(u"rightFrame")
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
        self.widget_4 = QWidget(self.rightFrame)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setSpacing(30)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(50, 30, 50, -1)
        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QVBoxLayout(self.widget_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.helloLabel = QLabel(self.widget_5)
        self.helloLabel.setObjectName(u"helloLabel")
        sizePolicy1.setHeightForWidth(self.helloLabel.sizePolicy().hasHeightForWidth())
        self.helloLabel.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.helloLabel.setFont(font)
        self.helloLabel.setStyleSheet(u"")
        self.helloLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.helloLabel)

        self.label = QLabel(self.widget_5)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(11)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"#label{\n"
"                                                                color: rgba(255, 255, 255, 192)}\n"
"                                                            ")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label)


        self.verticalLayout_6.addWidget(self.widget_5)

        self.signupButton = QPushButton(self.widget_4)
        self.signupButton.setObjectName(u"signupButton")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(False)
        self.signupButton.setFont(font2)
        self.signupButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.signupButton.setStyleSheet(u"#signupButton{\n"
"                                                    border-radius: 18px;\n"
"                                                    border:1px solid rgba(255, 255, 255, 150);\n"
"                                                    padding: 7px 0;\n"
"                                                    }\n"
"\n"
"                                                    #signupButton:hover{\n"
"                                                    border:1px solid #fff;\n"
"                                                    background: rgba(255, 255, 255, 30);\n"
"                                                    }\n"
"                                                ")

        self.verticalLayout_6.addWidget(self.signupButton)


        self.verticalLayout_5.addWidget(self.widget_4)


        self.mainLayout.addWidget(self.rightFrame)

        self.mainLayout.setStretch(0, 1)
        self.mainLayout.setStretch(1, 1)

        self.retranslateUi(login_form_main_window)

        QMetaObject.connectSlotsByName(login_form_main_window)
    # setupUi

    def retranslateUi(self, login_form_main_window):
        login_form_main_window.setWindowTitle(QCoreApplication.translate("login_form_main_window", u"Login", None))
        self.loginLabel.setText(QCoreApplication.translate("login_form_main_window", u"Welcome Back", None))
        self.loginSloganLabel.setText(QCoreApplication.translate("login_form_main_window", u"Please sign in to continue", None))
        self.usernameLabel.setText(QCoreApplication.translate("login_form_main_window", u"Username", None))
        self.passwordLabel.setText(QCoreApplication.translate("login_form_main_window", u"Password", None))
        self.erroLabel.setText("")
        self.loginButton.setText(QCoreApplication.translate("login_form_main_window", u"Login", None))
        self.helloLabel.setText(QCoreApplication.translate("login_form_main_window", u"New Here?", None))
        self.label.setText(QCoreApplication.translate("login_form_main_window", u"Create an account to get started.", None))
        self.signupButton.setText(QCoreApplication.translate("login_form_main_window", u"Sign up", None))
    # retranslateUi

