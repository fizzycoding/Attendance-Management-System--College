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
        self.sidebarFrame.setMaximumSize(QSize(220, 16777215))
        self.sidebarFrame.setStyleSheet(
            "#sidebarFrame {\n"
            "    background: qlineargradient(\n"
            "        x1:0, y1:0,\n"
            "        x2:0, y2:1,\n"
            "        stop:0 #50d5b7,\n"
            "        stop:1 #067d68\n"
            "    );\n"
            "}\n"
            "\n"
            "/* Base style for all sidebar buttons */\n"
            "QPushButton {\n"
            "    background-color: transparent;\n"
            "    color: white;\n"
            "    text-align: left;\n"
            "    padding-left: 20px;\n"
            "    border: none;\n"
            "    font-size: 14px;\n"
            "    font-weight: 500;\n"
            "    height: 45px;\n"
            "    border-left: 5px solid transparent;\n"
            "	qproperty-cursor: PointingHandCursor;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #159079;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    background-color: #159079;\n"
            "    border-left: 5px solid #ffffff;\n"
            "    font-weight: bold;\n"
            "}"
        )
        self.sidebarFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.sidebarFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.sidebarFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 20)
        self.logoFrame = QFrame(self.sidebarFrame)
        self.logoFrame.setObjectName("logoFrame")
        self.logoFrame.setMinimumSize(QSize(0, 100))
        self.logoFrame.setStyleSheet(
            "#logoFrame{\n"
            "	background: transparent;\n"
            "	border: 1px solid transparent;\n"
            "	border-bottom-color: rgba(255, 255, 255, 158)\n"
            "}"
        )
        self.horizontalLayout_2 = QHBoxLayout(self.logoFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.appTitle = QLabel(self.logoFrame)
        self.appTitle.setObjectName("appTitle")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.appTitle.setFont(font)
        self.appTitle.setStyleSheet("color: white;")
        self.appTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.appTitle)

        self.verticalLayout.addWidget(self.logoFrame)

        self.sidebarStack = QStackedWidget(self.sidebarFrame)
        self.sidebarStack.setObjectName("sidebarStack")
        self.studentPage = QWidget()
        self.studentPage.setObjectName("studentPage")
        self.verticalLayout_student = QVBoxLayout(self.studentPage)
        self.verticalLayout_student.setSpacing(5)
        self.verticalLayout_student.setObjectName("verticalLayout_student")
        self.verticalLayout_student.setContentsMargins(0, 10, 0, 0)
        self.btn_std_dashboard = QPushButton(self.studentPage)
        self.btn_std_dashboard.setObjectName("btn_std_dashboard")
        self.btn_std_dashboard.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile("icons/dashboard.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_std_dashboard.setIcon(icon)
        self.btn_std_dashboard.setIconSize(QSize(20, 20))
        self.btn_std_dashboard.setCheckable(True)
        self.btn_std_dashboard.setChecked(True)
        self.btn_std_dashboard.setAutoExclusive(True)

        self.verticalLayout_student.addWidget(self.btn_std_dashboard)

        self.btn_std_classes = QPushButton(self.studentPage)
        self.btn_std_classes.setObjectName("btn_std_classes")
        self.btn_std_classes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile("icons/class.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_std_classes.setIcon(icon1)
        self.btn_std_classes.setIconSize(QSize(20, 20))
        self.btn_std_classes.setCheckable(True)
        self.btn_std_classes.setAutoExclusive(True)

        self.verticalLayout_student.addWidget(self.btn_std_classes)

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
        self.btn_teach_dashboard.setIcon(icon)
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
        icon2 = QIcon()
        icon2.addFile(
            "icons/attendance.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.btn_teach_attendance.setIcon(icon2)
        self.btn_teach_attendance.setIconSize(QSize(20, 20))
        self.btn_teach_attendance.setCheckable(True)
        self.btn_teach_attendance.setAutoExclusive(True)

        self.verticalLayout_teacher.addWidget(self.btn_teach_attendance)

        self.btn_results = QPushButton(self.teacherPage)
        self.btn_results.setObjectName("btn_results")
        self.btn_results.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile("icons/test.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_results.setIcon(icon3)
        self.btn_results.setIconSize(QSize(20, 20))
        self.btn_results.setCheckable(True)
        self.btn_results.setAutoExclusive(True)
        self.btn_results.setAutoDefault(True)

        self.verticalLayout_teacher.addWidget(self.btn_results)

        self.btn_teach_reports = QPushButton(self.teacherPage)
        self.btn_teach_reports.setObjectName("btn_teach_reports")
        self.btn_teach_reports.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_teach_reports.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        icon4 = QIcon()
        icon4.addFile("icons/reports.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_teach_reports.setIcon(icon4)
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
        self.logoutButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.logoutButton.setStyleSheet(
            "\n"
            "QPushButton {\n"
            "    background-color: rgba(0,0,0,0.1);\n"
            "    color: #e0e0e0;\n"
            "}\n"
            "QPushButton:hover {\n"
            "    background-color: #c0392b; /* Red for logout */\n"
            "    color: white;\n"
            "}\n"
            ""
        )
        icon5 = QIcon()
        icon5.addFile("icons/logout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logoutButton.setIcon(icon5)
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
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.nameLabel.sizePolicy().hasHeightForWidth())
        self.nameLabel.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies(["Segoe UI"])
        font1.setPointSize(11)
        font1.setWeight(QFont.DemiBold)
        font1.setItalic(False)
        self.nameLabel.setFont(font1)
        self.nameLabel.setStyleSheet(
            "color: rgb(29, 29, 29);\n" 'font: 600 11pt "Segoe UI";'
        )

        self.verticalLayout_2.addWidget(self.nameLabel)

        self.usernameLabel = QLabel(self.headerFrame)
        self.usernameLabel.setObjectName("usernameLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.usernameLabel.sizePolicy().hasHeightForWidth()
        )
        self.usernameLabel.setSizePolicy(sizePolicy2)
        self.usernameLabel.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.usernameLabel.setStyleSheet(
            "color: rgb(75, 75, 75);\n" 'font: 600 9pt "Segoe UI";'
        )

        self.verticalLayout_2.addWidget(self.usernameLabel)

        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.label_2 = QLabel(self.headerFrame)
        self.label_2.setObjectName("label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
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
        self.appTitle.setText(
            QCoreApplication.translate("HomeWindow", "Academic Tracker", None)
        )
        self.btn_std_dashboard.setText(
            QCoreApplication.translate("HomeWindow", "Dashboard", None)
        )
        self.btn_std_classes.setText(
            QCoreApplication.translate("HomeWindow", "Classes", None)
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
