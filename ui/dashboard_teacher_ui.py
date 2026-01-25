# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboardTeacher.ui'
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
    QComboBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class Ui_dashboard_page(object):
    def setupUi(self, dashboard_page):
        if not dashboard_page.objectName():
            dashboard_page.setObjectName("dashboard_page")
        dashboard_page.resize(1029, 652)
        dashboard_page.setStyleSheet(
            "background-color: rgb(240, 240, 240);\n" 'font-family: "Segoe UI";'
        )
        self.verticalLayout = QVBoxLayout(dashboard_page)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.header_widget = QWidget(dashboard_page)
        self.header_widget.setObjectName("header_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.header_widget.sizePolicy().hasHeightForWidth()
        )
        self.header_widget.setSizePolicy(sizePolicy)
        self.header_widget.setStyleSheet("background-color: transparent")
        self.horizontalLayout_2 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.dropdown_classes = QComboBox(self.header_widget)
        self.dropdown_classes.setObjectName("dropdown_classes")
        self.dropdown_classes.setMinimumSize(QSize(200, 40))
        self.dropdown_classes.setStyleSheet(
            "QComboBox {\n"
            "    background-color: white;\n"
            "    border: 1px solid #ccc;\n"
            "    border-radius: 5px;\n"
            "    padding: 5px 10px;\n"
            "    font-size: 14px;\n"
            "    color: #333;\n"
            "}\n"
            "QComboBox::down-arrow {\n"
            "    image: url(icons/arrow_down.png); \n"
            "    width: 12px;\n"
            "    height: 12px;\n"
            "}\n"
            "QComboBox::drop-down {\n"
            "    subcontrol-origin: padding;\n"
            "    subcontrol-position: top right;\n"
            "    width: 30px;\n"
            "    border-left-width: 1px;\n"
            "    border-left-color: #ccc;\n"
            "    border-left-style: solid; \n"
            "    border-top-right-radius: 5px;\n"
            "    border-bottom-right-radius: 5px;\n"
            "    background: #f0f0f0; \n"
            "}\n"
            "QComboBox QAbstractItemView {\n"
            "    background-color: white;\n"
            "    border: 1px solid #ccc;\n"
            "    selection-color: #159079;\n"
            "    outline: 0;\n"
            "    color: rgb(0, 0, 0);\n"
            "}"
        )

        self.horizontalLayout_2.addWidget(self.dropdown_classes)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout.addWidget(self.header_widget)

        self.layout_main_content = QHBoxLayout()
        self.layout_main_content.setSpacing(10)
        self.layout_main_content.setObjectName("layout_main_content")
        self.layout_left_col = QVBoxLayout()
        self.layout_left_col.setSpacing(10)
        self.layout_left_col.setObjectName("layout_left_col")
        self.layout_cards = QHBoxLayout()
        self.layout_cards.setSpacing(10)
        self.layout_cards.setObjectName("layout_cards")
        self.card_present = QFrame(dashboard_page)
        self.card_present.setObjectName("card_present")
        self.card_present.setMaximumSize(QSize(16777215, 120))
        self.card_present.setStyleSheet(
            "QFrame { background-color: white; border-radius: 10px; border: 1px solid #e0e0e0; }\n"
            "QFrame:hover { border: 1px solid #57e700; }"
        )
        self.vbox_card2 = QVBoxLayout(self.card_present)
        self.vbox_card2.setObjectName("vbox_card2")
        self.pushButton_2 = QPushButton(self.card_present)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet(
            "color: #777; font-size: 11px; border:none;\n"
            "  font: 600 11pt; background-color: transparent; text-align: left"
        )
        icon = QIcon()
        icon.addFile("icons/students.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(18, 18))

        self.vbox_card2.addWidget(self.pushButton_2)

        self.val_total_student = QLabel(self.card_present)
        self.val_total_student.setObjectName("val_total_student")
        self.val_total_student.setStyleSheet(
            "color: #333;\n" "font-size:25pt; font-weight: bold; border:none;"
        )
        self.val_total_student.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.vbox_card2.addWidget(self.val_total_student)

        self.layout_cards.addWidget(self.card_present)

        self.card_total_classes = QFrame(dashboard_page)
        self.card_total_classes.setObjectName("card_total_classes")
        self.card_total_classes.setMaximumSize(QSize(16777215, 120))
        self.card_total_classes.setStyleSheet(
            "QFrame { background-color: white; border-radius: 10px; border: 1px solid #e0e0e0; }\n"
            "QFrame:hover { border: 1px solid #3388FF; }"
        )
        self.vbox_card1 = QVBoxLayout(self.card_total_classes)
        self.vbox_card1.setObjectName("vbox_card1")
        self.pushButton = QPushButton(self.card_total_classes)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet(
            "color: #777; font-size: 11px; border:none;\n"
            "  font: 600 11pt; background-color: transparent; text-align: left"
        )
        icon1 = QIcon()
        icon1.addFile("icons/board.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(16, 16))

        self.vbox_card1.addWidget(self.pushButton)

        self.val_total_classes = QLabel(self.card_total_classes)
        self.val_total_classes.setObjectName("val_total_classes")
        self.val_total_classes.setStyleSheet(
            "color: #333; font-size: 25pt; font-weight: bold; border:none;"
        )
        self.val_total_classes.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.vbox_card1.addWidget(self.val_total_classes)

        self.layout_cards.addWidget(self.card_total_classes)

        self.card_tests = QFrame(dashboard_page)
        self.card_tests.setObjectName("card_tests")
        self.card_tests.setMaximumSize(QSize(16777215, 120))
        self.card_tests.setStyleSheet(
            "QFrame { background-color: white; border-radius: 10px; border: 1px solid #e0e0e0; }\n"
            "QFrame:hover { border: 1px solid #d400e7; }"
        )
        self.vbox_card4 = QVBoxLayout(self.card_tests)
        self.vbox_card4.setObjectName("vbox_card4")
        self.pushButton_4 = QPushButton(self.card_tests)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet(
            "color: #777; font-size: 11px; border:none;\n"
            "  font: 600 11pt; background-color: transparent; text-align: left"
        )
        icon2 = QIcon()
        icon2.addFile(
            "icons/total_test.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QSize(18, 18))

        self.vbox_card4.addWidget(self.pushButton_4)

        self.val_tests = QLabel(self.card_tests)
        self.val_tests.setObjectName("val_tests")
        self.val_tests.setStyleSheet(
            "color: #333; font-size: 25pt; font-weight: bold; border:none;"
        )
        self.val_tests.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.vbox_card4.addWidget(self.val_tests)

        self.layout_cards.addWidget(self.card_tests)

        self.card_average_attendance = QFrame(dashboard_page)
        self.card_average_attendance.setObjectName("card_average_attendance")
        self.card_average_attendance.setMaximumSize(QSize(16777215, 120))
        self.card_average_attendance.setStyleSheet(
            "QFrame { background-color: white; border-radius: 10px; border: 1px solid #e0e0e0; }\n"
            "QFrame:hover { border: 1px solid #e7c100; }"
        )
        self.vbox_card3 = QVBoxLayout(self.card_average_attendance)
        self.vbox_card3.setObjectName("vbox_card3")
        self.pushButton_3 = QPushButton(self.card_average_attendance)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet(
            "color: #777; font-size: 11px; border:none;\n"
            "  font: 600 11pt; background-color: transparent; text-align: left"
        )
        icon3 = QIcon()
        icon3.addFile(
            "icons/average_attendance.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QSize(18, 18))

        self.vbox_card3.addWidget(self.pushButton_3)

        self.val_avg_attendance = QLabel(self.card_average_attendance)
        self.val_avg_attendance.setObjectName("val_avg_attendance")
        self.val_avg_attendance.setStyleSheet(
            "color: #333; font-size: 25pt; font-weight: bold; border:none;"
        )
        self.val_avg_attendance.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.vbox_card3.addWidget(self.val_avg_attendance)

        self.layout_cards.addWidget(self.card_average_attendance)

        self.layout_left_col.addLayout(self.layout_cards)

        self.frame_weekly = QFrame(dashboard_page)
        self.frame_weekly.setObjectName("frame_weekly")
        self.frame_weekly.setStyleSheet(
            "background-color: white; border-radius: 10px; border: 1px solid #e0e0e0;"
        )
        self.vbox_weekly = QVBoxLayout(self.frame_weekly)
        self.vbox_weekly.setObjectName("vbox_weekly")
        self.pushButton_5 = QPushButton(self.frame_weekly)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet(
            "font-size: 16px; font-weight: bold; color: #333; border:none;background-color:transparent; text-align: left"
        )
        icon4 = QIcon()
        icon4.addFile("icons/barChart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QSize(20, 20))

        self.vbox_weekly.addWidget(self.pushButton_5)

        self.chart_weekly_container = QWidget(self.frame_weekly)
        self.chart_weekly_container.setObjectName("chart_weekly_container")
        self.chart_weekly_container.setMinimumSize(QSize(0, 180))

        self.vbox_weekly.addWidget(self.chart_weekly_container)

        self.layout_left_col.addWidget(self.frame_weekly)

        self.layout_left_col.setStretch(1, 1)

        self.layout_main_content.addLayout(self.layout_left_col)

        self.layout_right_col = QVBoxLayout()
        self.layout_right_col.setSpacing(10)
        self.layout_right_col.setObjectName("layout_right_col")
        self.frame_leaderboard = QFrame(dashboard_page)
        self.frame_leaderboard.setObjectName("frame_leaderboard")
        self.frame_leaderboard.setMinimumSize(QSize(280, 0))
        self.frame_leaderboard.setStyleSheet(
            "background-color: white; border-radius: 10px; border: 1px solid #e0e0e0;"
        )
        self.vbox_leaderboard = QVBoxLayout(self.frame_leaderboard)
        self.vbox_leaderboard.setObjectName("vbox_leaderboard")
        self.pushButton_7 = QPushButton(self.frame_leaderboard)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setStyleSheet(
            "font-size: 16px; font-weight: bold; color: #333; margin-bottom: 5px; border:none;"
        )
        icon5 = QIcon()
        icon5.addFile(
            "icons/top_student.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.pushButton_7.setIcon(icon5)
        self.pushButton_7.setIconSize(QSize(16, 16))

        self.vbox_leaderboard.addWidget(self.pushButton_7)

        self.scrollArea_students = QScrollArea(self.frame_leaderboard)
        self.scrollArea_students.setObjectName("scrollArea_students")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.scrollArea_students.sizePolicy().hasHeightForWidth()
        )
        self.scrollArea_students.setSizePolicy(sizePolicy1)
        self.scrollArea_students.setWidgetResizable(True)
        self.scroll_content_students = QWidget()
        self.scroll_content_students.setObjectName("scroll_content_students")
        self.scroll_content_students.setGeometry(QRect(0, 0, 304, 219))
        self.container_top_students = QVBoxLayout(self.scroll_content_students)
        self.container_top_students.setSpacing(5)
        self.container_top_students.setObjectName("container_top_students")
        self.scrollArea_students.setWidget(self.scroll_content_students)

        self.vbox_leaderboard.addWidget(self.scrollArea_students)

        self.layout_right_col.addWidget(self.frame_leaderboard)

        self.frame_today_pie = QFrame(dashboard_page)
        self.frame_today_pie.setObjectName("frame_today_pie")
        self.frame_today_pie.setStyleSheet(
            "background-color: white; border-radius: 10px; border: 1px solid #e0e0e0;"
        )
        self.vbox_pie = QVBoxLayout(self.frame_today_pie)
        self.vbox_pie.setObjectName("vbox_pie")
        self.label_pie_title = QLabel(self.frame_today_pie)
        self.label_pie_title.setObjectName("label_pie_title")
        sizePolicy.setHeightForWidth(
            self.label_pie_title.sizePolicy().hasHeightForWidth()
        )
        self.label_pie_title.setSizePolicy(sizePolicy)
        self.label_pie_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vbox_pie.addWidget(self.label_pie_title)

        self.chart_pie_container = QWidget(self.frame_today_pie)
        self.chart_pie_container.setObjectName("chart_pie_container")

        self.vbox_pie.addWidget(self.chart_pie_container)

        self.layout_right_col.addWidget(self.frame_today_pie)

        self.layout_main_content.addLayout(self.layout_right_col)

        self.layout_main_content.setStretch(0, 2)
        self.layout_main_content.setStretch(1, 1)

        self.verticalLayout.addLayout(self.layout_main_content)

        self.retranslateUi(dashboard_page)

        QMetaObject.connectSlotsByName(dashboard_page)

    # setupUi

    def retranslateUi(self, dashboard_page):
        dashboard_page.setWindowTitle(
            QCoreApplication.translate("dashboard_page", "Teacher Dashboard", None)
        )
        self.dropdown_classes.setPlaceholderText(
            QCoreApplication.translate("dashboard_page", "Select Class", None)
        )
        self.pushButton_2.setText(
            QCoreApplication.translate("dashboard_page", "Total Students", None)
        )
        self.val_total_student.setText(
            QCoreApplication.translate("dashboard_page", "00", None)
        )
        self.pushButton.setText(
            QCoreApplication.translate("dashboard_page", "Total Classes", None)
        )
        self.val_total_classes.setText(
            QCoreApplication.translate("dashboard_page", "00", None)
        )
        self.pushButton_4.setText(
            QCoreApplication.translate("dashboard_page", "Tests Conducted", None)
        )
        self.val_tests.setText(QCoreApplication.translate("dashboard_page", "00", None))
        self.pushButton_3.setText(
            QCoreApplication.translate("dashboard_page", "Avg. Attendace", None)
        )
        self.val_avg_attendance.setText(
            QCoreApplication.translate("dashboard_page", "00%", None)
        )
        self.pushButton_5.setText(
            QCoreApplication.translate(
                "dashboard_page", "Weekly Attendance Report", None
            )
        )
        self.chart_weekly_container.setStyleSheet(
            QCoreApplication.translate("dashboard_page", "border:none;", None)
        )
        self.pushButton_7.setText(
            QCoreApplication.translate("dashboard_page", "Top Students", None)
        )
        self.scrollArea_students.setStyleSheet(
            QCoreApplication.translate(
                "dashboard_page", "border:none; background:transparent;", None
            )
        )
        self.label_pie_title.setStyleSheet(
            QCoreApplication.translate(
                "dashboard_page",
                "font-size: 16px; font-weight: bold; color: #333; border:none;",
                None,
            )
        )
        self.label_pie_title.setText(
            QCoreApplication.translate("dashboard_page", "Today's Report", None)
        )
        self.chart_pie_container.setStyleSheet(
            QCoreApplication.translate("dashboard_page", "border:none;", None)
        )

    # retranslateUi
