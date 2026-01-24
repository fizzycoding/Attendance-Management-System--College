# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
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
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_HomeWindow(object):
    def setupUi(self, HomeWindow):
        if not HomeWindow.objectName():
            HomeWindow.setObjectName("HomeWindow")
        HomeWindow.resize(1024, 700)
        HomeWindow.setStyleSheet(
            "#HomeWindow {\n" "   background-color: #f5f7fa;\n" "}"
        )
        self.horizontalLayout = QHBoxLayout(HomeWindow)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebarFrame = QFrame(HomeWindow)
        self.sidebarFrame.setObjectName("sidebarFrame")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebarFrame.sizePolicy().hasHeightForWidth())
        self.sidebarFrame.setSizePolicy(sizePolicy)
        self.sidebarFrame.setMinimumSize(QSize(220, 0))
        self.sidebarFrame.setMaximumSize(QSize(250, 16777215))
        self.sidebarFrame.setStyleSheet(
            "#sidebarFrame {\n"
            "    background: white;\n"
            "    border-right: 1px solid #e0e0e0;\n"
            "}\n"
            "\n"
            "/* Base style for all sidebar buttons */\n"
            "QPushButton {\n"
            "    background-color: transparent;\n"
            "    color: rgb(65, 65, 65);\n"
            "    text-align: left;\n"
            "    padding-left: 14px;\n"
            "    border: none;\n"
            "    font-size: 14px;\n"
            "    font-weight: 600;\n"
            "    height: 40px;\n"
            "    border-left: 5px solid transparent;\n"
            "	qproperty-cursor: PointingHandCursor;\n"
            "border-radius: 8px\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "	color: black\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    background-color: rgba(0, 85, 255, 35);\n"
            "    font-weight: 700;\n"
            "color: #3388FF\n"
            "}"
        )
        self.sidebarFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.sidebarFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.sidebarFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(15, 0, 15, 20)
        self.logoFrame = QFrame(self.sidebarFrame)
        self.logoFrame.setObjectName("logoFrame")
        self.logoFrame.setMinimumSize(QSize(0, 80))
        self.logoFrame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.logoFrame.setStyleSheet("#logoFrame{\n" "	background: transparent;\n" "}")
        self.horizontalLayout_2 = QHBoxLayout(self.logoFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.logoFrame)
        self.pushButton.setObjectName("pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButton.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            'font: 700 15pt "Segoe UI";\n'
            "border: none;\n"
            "   padding-left: 0px;"
        )
        icon = QIcon()
        icon.addFile("icons/logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.verticalLayout.addWidget(self.logoFrame)

        self.sidebarStack = QStackedWidget(self.sidebarFrame)
        self.sidebarStack.setObjectName("sidebarStack")
        self.studentPage = QWidget()
        self.studentPage.setObjectName("studentPage")
        self.verticalLayout_student = QVBoxLayout(self.studentPage)
        self.verticalLayout_student.setSpacing(5)
        self.verticalLayout_student.setObjectName("verticalLayout_student")
        self.verticalLayout_student.setContentsMargins(0, 10, 0, 0)
        self.btn_std_my_classes = QPushButton(self.studentPage)
        self.btn_std_my_classes.setObjectName("btn_std_my_classes")
        self.btn_std_my_classes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(
            "icons/class_unchecked.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        icon1.addFile("icons/class.png", QSize(), QIcon.Mode.Active, QIcon.State.On)
        self.btn_std_my_classes.setIcon(icon1)
        self.btn_std_my_classes.setIconSize(QSize(18, 18))
        self.btn_std_my_classes.setCheckable(True)
        self.btn_std_my_classes.setChecked(True)
        self.btn_std_my_classes.setAutoExclusive(True)

        self.verticalLayout_student.addWidget(self.btn_std_my_classes)

        self.btn_std_test_results = QPushButton(self.studentPage)
        self.btn_std_test_results.setObjectName("btn_std_test_results")
        self.btn_std_test_results.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(
            "icons/test_unchecked.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        icon2.addFile("icons/test.png", QSize(), QIcon.Mode.Active, QIcon.State.On)
        self.btn_std_test_results.setIcon(icon2)
        self.btn_std_test_results.setIconSize(QSize(20, 20))
        self.btn_std_test_results.setCheckable(True)
        self.btn_std_test_results.setAutoExclusive(True)

        self.verticalLayout_student.addWidget(self.btn_std_test_results)

        self.verticalSpacer_std = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_student.addItem(self.verticalSpacer_std)

        self.sidebarStack.addWidget(self.studentPage)
        self.teacherPage = QWidget()
        self.teacherPage.setObjectName("teacherPage")
        self.verticalLayout_teacher = QVBoxLayout(self.teacherPage)
        self.verticalLayout_teacher.setSpacing(5)
        self.verticalLayout_teacher.setObjectName("verticalLayout_teacher")
        self.verticalLayout_teacher.setContentsMargins(0, 10, 0, 0)
        self.btn_teach_dashboard = QPushButton(self.teacherPage)
        self.btn_teach_dashboard.setObjectName("btn_teach_dashboard")
        self.btn_teach_dashboard.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_teach_dashboard.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon3 = QIcon()
        icon3.addFile(
            "icons/dashboard_unchecked.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        icon3.addFile("icons/dashboard.png", QSize(), QIcon.Mode.Active, QIcon.State.On)
        self.btn_teach_dashboard.setIcon(icon3)
        self.btn_teach_dashboard.setIconSize(QSize(20, 20))
        self.btn_teach_dashboard.setCheckable(True)
        self.btn_teach_dashboard.setChecked(True)
        self.btn_teach_dashboard.setAutoExclusive(True)

        self.verticalLayout_teacher.addWidget(self.btn_teach_dashboard)

        self.btn_teach_classes = QPushButton(self.teacherPage)
        self.btn_teach_classes.setObjectName("btn_teach_classes")
        self.btn_teach_classes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_teach_classes.setIcon(icon1)
        self.btn_teach_classes.setIconSize(QSize(20, 20))
        self.btn_teach_classes.setCheckable(True)
        self.btn_teach_classes.setAutoExclusive(True)

        self.verticalLayout_teacher.addWidget(self.btn_teach_classes)

        self.btn_teach_attendance = QPushButton(self.teacherPage)
        self.btn_teach_attendance.setObjectName("btn_teach_attendance")
        self.btn_teach_attendance.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(
            "icons/attendance_unchecked.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        icon4.addFile(
            "icons/attendance.png", QSize(), QIcon.Mode.Active, QIcon.State.On
        )
        self.btn_teach_attendance.setIcon(icon4)
        self.btn_teach_attendance.setIconSize(QSize(20, 20))
        self.btn_teach_attendance.setCheckable(True)
        self.btn_teach_attendance.setAutoExclusive(True)

        self.verticalLayout_teacher.addWidget(self.btn_teach_attendance)

        self.btn_results = QPushButton(self.teacherPage)
        self.btn_results.setObjectName("btn_results")
        self.btn_results.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_results.setIcon(icon2)
        self.btn_results.setIconSize(QSize(20, 20))
        self.btn_results.setCheckable(True)
        self.btn_results.setAutoExclusive(True)
        self.btn_results.setAutoDefault(True)

        self.verticalLayout_teacher.addWidget(self.btn_results)

        self.btn_teach_reports = QPushButton(self.teacherPage)
        self.btn_teach_reports.setObjectName("btn_teach_reports")
        self.btn_teach_reports.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_teach_reports.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        icon5 = QIcon()
        icon5.addFile(
            "icons/barChart_unchecked.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        icon5.addFile("icons/barChart.png", QSize(), QIcon.Mode.Active, QIcon.State.On)
        self.btn_teach_reports.setIcon(icon5)
        self.btn_teach_reports.setIconSize(QSize(20, 20))
        self.btn_teach_reports.setCheckable(True)
        self.btn_teach_reports.setAutoExclusive(True)
        self.btn_teach_reports.setAutoDefault(True)

        self.verticalLayout_teacher.addWidget(self.btn_teach_reports)

        self.verticalSpacer_teach = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_teacher.addItem(self.verticalSpacer_teach)

        self.sidebarStack.addWidget(self.teacherPage)

        self.verticalLayout.addWidget(self.sidebarStack)

        self.logoutButton = QPushButton(self.sidebarFrame)
        self.logoutButton.setObjectName("logoutButton")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.logoutButton.sizePolicy().hasHeightForWidth()
        )
        self.logoutButton.setSizePolicy(sizePolicy2)
        self.logoutButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.logoutButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.logoutButton.setStyleSheet(
            "\n" "QPushButton {\n" "    color: #ff1c57;\n" "}\n" ""
        )
        icon6 = QIcon()
        icon6.addFile("icons/logout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logoutButton.setIcon(icon6)
        self.logoutButton.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.logoutButton)

        self.horizontalLayout.addWidget(self.sidebarFrame)

        self.mainContentLayout = QVBoxLayout()
        self.mainContentLayout.setSpacing(0)
        self.mainContentLayout.setObjectName("mainContentLayout")
        self.headerFrame = QFrame(HomeWindow)
        self.headerFrame.setObjectName("headerFrame")
        self.headerFrame.setMinimumSize(QSize(0, 60))
        self.headerFrame.setStyleSheet(
            "#headerFrame {\n"
            "    background-color: white;\n"
            "    border-bottom: 1px solid #e0e0e0;\n"
            "}"
        )
        self.horizontalLayout_3 = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.nameLabel = QLabel(self.headerFrame)
        self.nameLabel.setObjectName("nameLabel")
        sizePolicy2.setHeightForWidth(self.nameLabel.sizePolicy().hasHeightForWidth())
        self.nameLabel.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamilies(["Segoe UI"])
        font.setPointSize(11)
        font.setWeight(QFont.DemiBold)
        font.setItalic(False)
        self.nameLabel.setFont(font)
        self.nameLabel.setStyleSheet(
            "color: rgb(29, 29, 29);\n" 'font: 600 11pt "Segoe UI";'
        )

        self.verticalLayout_2.addWidget(self.nameLabel)

        self.usernameLabel = QLabel(self.headerFrame)
        self.usernameLabel.setObjectName("usernameLabel")
        sizePolicy1.setHeightForWidth(
            self.usernameLabel.sizePolicy().hasHeightForWidth()
        )
        self.usernameLabel.setSizePolicy(sizePolicy1)
        self.usernameLabel.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.usernameLabel.setStyleSheet(
            "color: rgb(75, 75, 75);\n" 'font: 600 9pt "Segoe UI";'
        )

        self.verticalLayout_2.addWidget(self.usernameLabel)

        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.label_2 = QLabel(self.headerFrame)
        self.label_2.setObjectName("label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(42, 42))
        self.label_2.setMaximumSize(QSize(42, 42))
        self.label_2.setPixmap(QPixmap("icons/pfp.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.mainContentLayout.addWidget(self.headerFrame)

        self.mainContentStack = QStackedWidget(HomeWindow)
        self.mainContentStack.setObjectName("mainContentStack")
        self.mainContentStack.setStyleSheet("background: rgb(248, 248, 248)")
        self.pageDashboard = QWidget()
        self.pageDashboard.setObjectName("pageDashboard")
        self.verticalLayout_3 = QVBoxLayout(self.pageDashboard)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.mainContentStack.addWidget(self.pageDashboard)

        self.mainContentLayout.addWidget(self.mainContentStack)

        self.horizontalLayout.addLayout(self.mainContentLayout)

        self.retranslateUi(HomeWindow)

        self.sidebarStack.setCurrentIndex(1)
        self.btn_teach_reports.setDefault(False)
        self.mainContentStack.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(HomeWindow)

    # setupUi

    def retranslateUi(self, HomeWindow):
        HomeWindow.setWindowTitle(
            QCoreApplication.translate("HomeWindow", "Dashboard", None)
        )
        self.pushButton.setText(
            QCoreApplication.translate("HomeWindow", "Academic Tracker", None)
        )
        self.btn_std_my_classes.setText(
            QCoreApplication.translate("HomeWindow", "My Classes", None)
        )
        self.btn_std_test_results.setText(
            QCoreApplication.translate("HomeWindow", "Test Results", None)
        )
        self.btn_teach_dashboard.setText(
            QCoreApplication.translate("HomeWindow", "Dashboard", None)
        )
        self.btn_teach_classes.setText(
            QCoreApplication.translate("HomeWindow", "Classes", None)
        )
        self.btn_teach_attendance.setText(
            QCoreApplication.translate("HomeWindow", "Attendance", None)
        )
        self.btn_results.setText(
            QCoreApplication.translate("HomeWindow", "Test Results", None)
        )
        self.btn_teach_reports.setText(
            QCoreApplication.translate("HomeWindow", "View Reports", None)
        )
        self.logoutButton.setText(
            QCoreApplication.translate("HomeWindow", "Logout", None)
        )
        self.nameLabel.setText(
            QCoreApplication.translate("HomeWindow", "Kirtiman Patel", None)
        )
        self.usernameLabel.setText(
            QCoreApplication.translate("HomeWindow", "sanju789", None)
        )
        self.label_2.setText("")

    # retranslateUi
