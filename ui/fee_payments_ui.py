# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'feePayments.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_FeesPaymentPage(object):
    def setupUi(self, FeesPaymentPage):
        if not FeesPaymentPage.objectName():
            FeesPaymentPage.setObjectName(u"FeesPaymentPage")
        FeesPaymentPage.resize(900, 595)
        FeesPaymentPage.setStyleSheet(u"\n"
"background-color: rgb(235, 235, 235);\n"
"font-family: \"Segoe UI\";\n"
"   ")
        self.mainLayout = QVBoxLayout(FeesPaymentPage)
        self.mainLayout.setSpacing(12)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(16, 16, 16, 16)
        self.header_widget = QWidget(FeesPaymentPage)
        self.header_widget.setObjectName(u"header_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_widget.sizePolicy().hasHeightForWidth())
        self.header_widget.setSizePolicy(sizePolicy)
        self.header_widget.setMinimumSize(QSize(0, 52))
        self.header_widget.setStyleSheet(u"background: transparent;")
        self.headerLayout = QHBoxLayout(self.header_widget)
        self.headerLayout.setObjectName(u"headerLayout")
        self.headerLayout.setContentsMargins(0, 0, 0, 0)
        self.dropdown_classes = QComboBox(self.header_widget)
        self.dropdown_classes.setObjectName(u"dropdown_classes")
        self.dropdown_classes.setMinimumSize(QSize(200, 40))
        self.dropdown_classes.setStyleSheet(u"QComboBox {\n"
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
"}")

        self.headerLayout.addWidget(self.dropdown_classes)

        self.headerSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.headerLayout.addItem(self.headerSpacer)

        self.pageTitle = QLabel(self.header_widget)
        self.pageTitle.setObjectName(u"pageTitle")
        self.pageTitle.setStyleSheet(u"\n"
"font-size: 18px;\n"
"font-weight: 600;\n"
"color: #222;\n"
"         ")
        self.pageTitle.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.headerLayout.addWidget(self.pageTitle)


        self.mainLayout.addWidget(self.header_widget)

        self.cards_widget = QWidget(FeesPaymentPage)
        self.cards_widget.setObjectName(u"cards_widget")
        self.cards_widget.setMinimumSize(QSize(0, 0))
        self.cards_widget.setStyleSheet(u"background: transparent;")
        self.cardsLayout = QHBoxLayout(self.cards_widget)
        self.cardsLayout.setSpacing(12)
        self.cardsLayout.setObjectName(u"cardsLayout")
        self.cardsLayout.setContentsMargins(0, 0, 0, 0)
        self.card_totalFees = QFrame(self.cards_widget)
        self.card_totalFees.setObjectName(u"card_totalFees")
        sizePolicy.setHeightForWidth(self.card_totalFees.sizePolicy().hasHeightForWidth())
        self.card_totalFees.setSizePolicy(sizePolicy)
        self.card_totalFees.setMinimumSize(QSize(0, 0))
        self.card_totalFees.setStyleSheet(u"QFrame {\n"
"    background-color: white;\n"
"    border: 1px solid #bbb;\n"
"    border-radius: 12px;\n"
"}\n"
"QFrame:hover{\n"
"	border: 1px solid #3388FF;\n"
"}         ")
        self.totalFeesLayout = QVBoxLayout(self.card_totalFees)
        self.totalFeesLayout.setObjectName(u"totalFeesLayout")
        self.totalFeesLayout.setContentsMargins(14, 12, 14, 12)
        self.label_totalFeesTitle = QLabel(self.card_totalFees)
        self.label_totalFeesTitle.setObjectName(u"label_totalFeesTitle")
        sizePolicy.setHeightForWidth(self.label_totalFeesTitle.sizePolicy().hasHeightForWidth())
        self.label_totalFeesTitle.setSizePolicy(sizePolicy)
        self.label_totalFeesTitle.setStyleSheet(u"font-size: 13px; color: #666; border: none;")

        self.totalFeesLayout.addWidget(self.label_totalFeesTitle)

        self.label_totalFeesValue = QLabel(self.card_totalFees)
        self.label_totalFeesValue.setObjectName(u"label_totalFeesValue")
        sizePolicy.setHeightForWidth(self.label_totalFeesValue.sizePolicy().hasHeightForWidth())
        self.label_totalFeesValue.setSizePolicy(sizePolicy)
        self.label_totalFeesValue.setStyleSheet(u"font-size: 22px; font-weight: 700; color: #111; border: none;")

        self.totalFeesLayout.addWidget(self.label_totalFeesValue)


        self.cardsLayout.addWidget(self.card_totalFees)

        self.card_paidAmount = QFrame(self.cards_widget)
        self.card_paidAmount.setObjectName(u"card_paidAmount")
        sizePolicy.setHeightForWidth(self.card_paidAmount.sizePolicy().hasHeightForWidth())
        self.card_paidAmount.setSizePolicy(sizePolicy)
        self.card_paidAmount.setMinimumSize(QSize(0, 0))
        self.card_paidAmount.setStyleSheet(u"\n"
"QFrame {\n"
"    background-color: white;\n"
"    border: 1px solid #bbb;\n"
"    border-radius: 12px;\n"
"}\n"
"         \n"
"QFrame:hover{\n"
"	border: 1px solid #3388FF;\n"
"}   ")
        self.paidAmountLayout = QVBoxLayout(self.card_paidAmount)
        self.paidAmountLayout.setSpacing(6)
        self.paidAmountLayout.setObjectName(u"paidAmountLayout")
        self.paidAmountLayout.setContentsMargins(14, 12, 14, 12)
        self.label_paidAmountTitle = QLabel(self.card_paidAmount)
        self.label_paidAmountTitle.setObjectName(u"label_paidAmountTitle")
        sizePolicy.setHeightForWidth(self.label_paidAmountTitle.sizePolicy().hasHeightForWidth())
        self.label_paidAmountTitle.setSizePolicy(sizePolicy)
        self.label_paidAmountTitle.setStyleSheet(u"font-size: 13px; color: #666; border: none;")

        self.paidAmountLayout.addWidget(self.label_paidAmountTitle)

        self.label_paidAmountValue = QLabel(self.card_paidAmount)
        self.label_paidAmountValue.setObjectName(u"label_paidAmountValue")
        sizePolicy.setHeightForWidth(self.label_paidAmountValue.sizePolicy().hasHeightForWidth())
        self.label_paidAmountValue.setSizePolicy(sizePolicy)
        self.label_paidAmountValue.setStyleSheet(u"font-size: 22px; font-weight: 700; color: #111; border: none;")

        self.paidAmountLayout.addWidget(self.label_paidAmountValue)


        self.cardsLayout.addWidget(self.card_paidAmount)

        self.card_pendingAmount = QFrame(self.cards_widget)
        self.card_pendingAmount.setObjectName(u"card_pendingAmount")
        sizePolicy.setHeightForWidth(self.card_pendingAmount.sizePolicy().hasHeightForWidth())
        self.card_pendingAmount.setSizePolicy(sizePolicy)
        self.card_pendingAmount.setMinimumSize(QSize(0, 0))
        self.card_pendingAmount.setStyleSheet(u"\n"
"QFrame {\n"
"    background-color: white;\n"
"    border: 1px solid #bbb;\n"
"    border-radius: 12px;\n"
"}\n"
"         \n"
"QFrame:hover{\n"
"	border: 1px solid #3388FF;\n"
"}   ")
        self.pendingAmountLayout = QVBoxLayout(self.card_pendingAmount)
        self.pendingAmountLayout.setObjectName(u"pendingAmountLayout")
        self.pendingAmountLayout.setContentsMargins(14, 12, 14, 12)
        self.label_pendingAmountTitle = QLabel(self.card_pendingAmount)
        self.label_pendingAmountTitle.setObjectName(u"label_pendingAmountTitle")
        sizePolicy.setHeightForWidth(self.label_pendingAmountTitle.sizePolicy().hasHeightForWidth())
        self.label_pendingAmountTitle.setSizePolicy(sizePolicy)
        self.label_pendingAmountTitle.setStyleSheet(u"font-size: 13px; color: #666; border: none;")

        self.pendingAmountLayout.addWidget(self.label_pendingAmountTitle)

        self.label_pendingAmountValue = QLabel(self.card_pendingAmount)
        self.label_pendingAmountValue.setObjectName(u"label_pendingAmountValue")
        sizePolicy.setHeightForWidth(self.label_pendingAmountValue.sizePolicy().hasHeightForWidth())
        self.label_pendingAmountValue.setSizePolicy(sizePolicy)
        self.label_pendingAmountValue.setStyleSheet(u"font-size: 22px; font-weight: 700; color: #111; border: none;")

        self.pendingAmountLayout.addWidget(self.label_pendingAmountValue)


        self.cardsLayout.addWidget(self.card_pendingAmount)


        self.mainLayout.addWidget(self.cards_widget)

        self.content_stack = QStackedWidget(FeesPaymentPage)
        self.content_stack.setObjectName(u"content_stack")
        self.content_stack.setStyleSheet(u"background-color: transparent;")
        self.no_student_page = QWidget()
        self.no_student_page.setObjectName(u"no_student_page")
        self.verticalLayout_empty = QVBoxLayout(self.no_student_page)
        self.verticalLayout_empty.setObjectName(u"verticalLayout_empty")
        self.label_no_student = QLabel(self.no_student_page)
        self.label_no_student.setObjectName(u"label_no_student")
        self.label_no_student.setStyleSheet(u"font: 15pt \"Segoe UI\"; color: rgb(100, 100, 100);")
        self.label_no_student.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_empty.addWidget(self.label_no_student)

        self.content_stack.addWidget(self.no_student_page)
        self.page_list = QWidget()
        self.page_list.setObjectName(u"page_list")
        self.verticalLayout_list = QVBoxLayout(self.page_list)
        self.verticalLayout_list.setSpacing(10)
        self.verticalLayout_list.setObjectName(u"verticalLayout_list")
        self.verticalLayout_list.setContentsMargins(0, 0, 0, 0)
        self.searchBarWidget = QWidget(self.page_list)
        self.searchBarWidget.setObjectName(u"searchBarWidget")
        self.searchBarWidget.setMinimumSize(QSize(0, 46))
        self.searchBarWidget.setStyleSheet(u"background: transparent;")
        self.searchBarLayout = QHBoxLayout(self.searchBarWidget)
        self.searchBarLayout.setSpacing(10)
        self.searchBarLayout.setObjectName(u"searchBarLayout")
        self.searchBarLayout.setContentsMargins(0, 0, 0, 0)
        self.input_searchStudent = QLineEdit(self.searchBarWidget)
        self.input_searchStudent.setObjectName(u"input_searchStudent")
        sizePolicy.setHeightForWidth(self.input_searchStudent.sizePolicy().hasHeightForWidth())
        self.input_searchStudent.setSizePolicy(sizePolicy)
        self.input_searchStudent.setMinimumSize(QSize(300, 40))
        self.input_searchStudent.setStyleSheet(u"\n"
"QLineEdit {\n"
"    background-color: white;\n"
"    border: 1px solid #bbb;\n"
"    border-radius: 10px;\n"
"    padding: 8px 12px;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #3388FF\n"
";\n"
"}\n"
"             ")

        self.searchBarLayout.addWidget(self.input_searchStudent)

        self.dropdown_statusFilter = QComboBox(self.searchBarWidget)
        self.dropdown_statusFilter.addItem("")
        self.dropdown_statusFilter.addItem("")
        self.dropdown_statusFilter.addItem("")
        self.dropdown_statusFilter.addItem("")
        self.dropdown_statusFilter.setObjectName(u"dropdown_statusFilter")
        sizePolicy.setHeightForWidth(self.dropdown_statusFilter.sizePolicy().hasHeightForWidth())
        self.dropdown_statusFilter.setSizePolicy(sizePolicy)
        self.dropdown_statusFilter.setMinimumSize(QSize(0, 40))
        self.dropdown_statusFilter.setStyleSheet(u"\n"
"QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid #bbb\n"
";\n"
"    border-radius: 10px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white;\n"
"    border: 1px solid #d0d0d0;\n"
"    selection-background-color: #e8f4ff;\n"
"    selection-color: #222;\n"
"    outline: 0;\n"
"color: #333\n"
"}\n"
"             ")

        self.searchBarLayout.addWidget(self.dropdown_statusFilter)

        self.searchSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.searchBarLayout.addItem(self.searchSpacer)

        self.set_fees_btn = QPushButton(self.searchBarWidget)
        self.set_fees_btn.setObjectName(u"set_fees_btn")
        self.set_fees_btn.setStyleSheet(u"#set_fees_btn{color: #fff;\n"
"background : #3388FF;\n"
"border: none;\n"
"padding: 10px 20px;\n"
"font: 600 14px \"Segoe UI\";\n"
"border-radius: 7px}\n"
"\n"
"#set_fees_btn:hover{\n"
"background : #0055FF;}")

        self.searchBarLayout.addWidget(self.set_fees_btn)


        self.verticalLayout_list.addWidget(self.searchBarWidget)

        self.container = QWidget(self.page_list)
        self.container.setObjectName(u"container")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.container.sizePolicy().hasHeightForWidth())
        self.container.setSizePolicy(sizePolicy1)
        self.container.setStyleSheet(u"#container{background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(187, 187, 187); border-radius: 10px}")
        self.verticalLayout = QVBoxLayout(self.container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tableHeader = QFrame(self.container)
        self.tableHeader.setObjectName(u"tableHeader")
        sizePolicy.setHeightForWidth(self.tableHeader.sizePolicy().hasHeightForWidth())
        self.tableHeader.setSizePolicy(sizePolicy)
        self.tableHeader.setMinimumSize(QSize(0, 0))
        self.tableHeader.setStyleSheet(u"QFrame{boder:none}\n"
"\n"
"QLabel {\n"
"    font-size: 12px;\n"
"    color: #555;\n"
"    font-weight: 600;\n"
"border: none\n"
"\n"
"}\n"
"          ")
        self.headerRowLayout = QHBoxLayout(self.tableHeader)
        self.headerRowLayout.setObjectName(u"headerRowLayout")
        self.headerRowLayout.setContentsMargins(12, 12, 12, 12)
        self.label = QLabel(self.tableHeader)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMinimumSize(QSize(60, 0))

        self.headerRowLayout.addWidget(self.label)

        self.head_student = QLabel(self.tableHeader)
        self.head_student.setObjectName(u"head_student")
        self.head_student.setMinimumSize(QSize(220, 0))

        self.headerRowLayout.addWidget(self.head_student)

        self.head_total = QLabel(self.tableHeader)
        self.head_total.setObjectName(u"head_total")

        self.headerRowLayout.addWidget(self.head_total)

        self.head_paid = QLabel(self.tableHeader)
        self.head_paid.setObjectName(u"head_paid")

        self.headerRowLayout.addWidget(self.head_paid)

        self.head_pending = QLabel(self.tableHeader)
        self.head_pending.setObjectName(u"head_pending")

        self.headerRowLayout.addWidget(self.head_pending)

        self.head_status = QLabel(self.tableHeader)
        self.head_status.setObjectName(u"head_status")
        self.head_status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.headerRowLayout.addWidget(self.head_status)

        self.head_action = QLabel(self.tableHeader)
        self.head_action.setObjectName(u"head_action")
        self.head_action.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.headerRowLayout.addWidget(self.head_action)


        self.verticalLayout.addWidget(self.tableHeader)

        self.students_list_container = QScrollArea(self.container)
        self.students_list_container.setObjectName(u"students_list_container")
        sizePolicy1.setHeightForWidth(self.students_list_container.sizePolicy().hasHeightForWidth())
        self.students_list_container.setSizePolicy(sizePolicy1)
        self.students_list_container.setStyleSheet(u"border:none\n"
"")
        self.students_list_container.setFrameShape(QFrame.Shape.NoFrame)
        self.students_list_container.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 868, 311))
        self.studentsLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.studentsLayout.setSpacing(0)
        self.studentsLayout.setObjectName(u"studentsLayout")
        self.studentsLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.studentsLayout.addItem(self.verticalSpacer)

        self.students_list_container.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.students_list_container)


        self.verticalLayout_list.addWidget(self.container)

        self.content_stack.addWidget(self.page_list)

        self.mainLayout.addWidget(self.content_stack)


        self.retranslateUi(FeesPaymentPage)

        self.content_stack.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(FeesPaymentPage)
    # setupUi

    def retranslateUi(self, FeesPaymentPage):
        FeesPaymentPage.setWindowTitle(QCoreApplication.translate("FeesPaymentPage", u"Fee Overview", None))
        self.pageTitle.setText(QCoreApplication.translate("FeesPaymentPage", u"Fee Overview", None))
        self.label_totalFeesTitle.setText(QCoreApplication.translate("FeesPaymentPage", u"Total Fees", None))
        self.label_totalFeesValue.setText(QCoreApplication.translate("FeesPaymentPage", u"\u20b90", None))
        self.label_paidAmountTitle.setText(QCoreApplication.translate("FeesPaymentPage", u"Paid Amount", None))
        self.label_paidAmountValue.setText(QCoreApplication.translate("FeesPaymentPage", u"\u20b90", None))
        self.label_pendingAmountTitle.setText(QCoreApplication.translate("FeesPaymentPage", u"Pending Amount", None))
        self.label_pendingAmountValue.setText(QCoreApplication.translate("FeesPaymentPage", u"\u20b90", None))
        self.label_no_student.setText(QCoreApplication.translate("FeesPaymentPage", u"No Students", None))
        self.input_searchStudent.setPlaceholderText(QCoreApplication.translate("FeesPaymentPage", u"Search student name...", None))
        self.dropdown_statusFilter.setItemText(0, QCoreApplication.translate("FeesPaymentPage", u"All", None))
        self.dropdown_statusFilter.setItemText(1, QCoreApplication.translate("FeesPaymentPage", u"Paid", None))
        self.dropdown_statusFilter.setItemText(2, QCoreApplication.translate("FeesPaymentPage", u"Partial", None))
        self.dropdown_statusFilter.setItemText(3, QCoreApplication.translate("FeesPaymentPage", u"Unpaid", None))

        self.set_fees_btn.setText(QCoreApplication.translate("FeesPaymentPage", u"Set Fees", None))
        self.label.setText(QCoreApplication.translate("FeesPaymentPage", u"S.No.", None))
        self.head_student.setText(QCoreApplication.translate("FeesPaymentPage", u"Student", None))
        self.head_total.setText(QCoreApplication.translate("FeesPaymentPage", u"Total Fee", None))
        self.head_paid.setText(QCoreApplication.translate("FeesPaymentPage", u"Paid", None))
        self.head_pending.setText(QCoreApplication.translate("FeesPaymentPage", u"Pending", None))
        self.head_status.setText(QCoreApplication.translate("FeesPaymentPage", u"Status", None))
        self.head_action.setText(QCoreApplication.translate("FeesPaymentPage", u"Action", None))
    # retranslateUi

