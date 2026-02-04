from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QCursor)
from PySide6.QtWidgets import (QComboBox, QFrame, QHBoxLayout,
                               QLabel, QPushButton, QScrollArea, QSizePolicy,
                               QSpacerItem, QVBoxLayout, QWidget)


class Ui_StudentFeesPage(object):
    def setupUi(self, StudentFeesPage):
        if not StudentFeesPage.objectName():
            StudentFeesPage.setObjectName(u"StudentFeesPage")
        StudentFeesPage.resize(900, 595)
        StudentFeesPage.setStyleSheet(u"\n"
                                      "background-color: rgb(235, 235, 235);\n"
                                      "font-family: \"Segoe UI\";\n"
                                      "   ")
        self.mainLayout = QVBoxLayout(StudentFeesPage)
        self.mainLayout.setSpacing(12)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(16, 16, 16, 16)
        self.header_widget = QWidget(StudentFeesPage)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setMinimumSize(QSize(0, 52))
        self.header_widget.setStyleSheet(u"background: transparent;")
        self.headerLayout = QHBoxLayout(self.header_widget)
        self.headerLayout.setObjectName(u"headerLayout")
        self.headerLayout.setContentsMargins(0, 0, 0, 0)
        self.dropdown_classes = QComboBox(self.header_widget)
        self.dropdown_classes.setObjectName(u"dropdown_classes")
        self.dropdown_classes.setMinimumSize(QSize(220, 40))
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
                                     "font-weight: 700;\n"
                                     "color: #222;\n"
                                     "         ")
        self.pageTitle.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTrailing | Qt.AlignmentFlag.AlignVCenter)

        self.headerLayout.addWidget(self.pageTitle)

        self.mainLayout.addWidget(self.header_widget)

        self.cards_widget = QWidget(StudentFeesPage)
        self.cards_widget.setObjectName(u"cards_widget")
        self.cards_widget.setStyleSheet(u"background: transparent;")
        self.cardsLayout = QHBoxLayout(self.cards_widget)
        self.cardsLayout.setSpacing(12)
        self.cardsLayout.setObjectName(u"cardsLayout")
        self.cardsLayout.setContentsMargins(0, 0, 0, 0)
        self.card_totalFees = QFrame(self.cards_widget)
        self.card_totalFees.setObjectName(u"card_totalFees")
        self.card_totalFees.setStyleSheet(u"QFrame {\n"
                                          "    background-color: white;\n"
                                          "    border: 1px solid #bbb;\n"
                                          "    border-radius: 12px;\n"
                                          "}\n"
                                          "QFrame:hover{\n"
                                          "    border: 1px solid #3388FF;\n"
                                          "}")
        self.totalFeesLayout = QVBoxLayout(self.card_totalFees)
        self.totalFeesLayout.setObjectName(u"totalFeesLayout")
        self.totalFeesLayout.setContentsMargins(14, 12, 14, 12)
        self.label_totalFeesTitle = QLabel(self.card_totalFees)
        self.label_totalFeesTitle.setObjectName(u"label_totalFeesTitle")
        self.label_totalFeesTitle.setStyleSheet(u"font-size: 13px; color: #666; border: none;")

        self.totalFeesLayout.addWidget(self.label_totalFeesTitle)

        self.label_totalFeesValue = QLabel(self.card_totalFees)
        self.label_totalFeesValue.setObjectName(u"label_totalFeesValue")
        self.label_totalFeesValue.setStyleSheet(u"font-size: 22px; font-weight: 800; color: #111; border: none;")

        self.totalFeesLayout.addWidget(self.label_totalFeesValue)

        self.cardsLayout.addWidget(self.card_totalFees)

        self.card_paidAmount = QFrame(self.cards_widget)
        self.card_paidAmount.setObjectName(u"card_paidAmount")
        self.card_paidAmount.setStyleSheet(u"QFrame {\n"
                                           "    background-color: white;\n"
                                           "    border: 1px solid #bbb;\n"
                                           "    border-radius: 12px;\n"
                                           "}\n"
                                           "QFrame:hover{\n"
                                           "    border: 1px solid #3388FF;\n"
                                           "}")
        self.paidAmountLayout = QVBoxLayout(self.card_paidAmount)
        self.paidAmountLayout.setObjectName(u"paidAmountLayout")
        self.paidAmountLayout.setContentsMargins(14, 12, 14, 12)
        self.label_paidAmountTitle = QLabel(self.card_paidAmount)
        self.label_paidAmountTitle.setObjectName(u"label_paidAmountTitle")
        self.label_paidAmountTitle.setStyleSheet(u"font-size: 13px; color: #666; border: none;")

        self.paidAmountLayout.addWidget(self.label_paidAmountTitle)

        self.label_paidAmountValue = QLabel(self.card_paidAmount)
        self.label_paidAmountValue.setObjectName(u"label_paidAmountValue")
        self.label_paidAmountValue.setStyleSheet(u"font-size: 22px; font-weight: 800; color: #111; border: none;")

        self.paidAmountLayout.addWidget(self.label_paidAmountValue)

        self.cardsLayout.addWidget(self.card_paidAmount)

        self.card_pendingAmount = QFrame(self.cards_widget)
        self.card_pendingAmount.setObjectName(u"card_pendingAmount")
        self.card_pendingAmount.setStyleSheet(u"QFrame {\n"
                                              "    background-color: white;\n"
                                              "    border: 1px solid #bbb;\n"
                                              "    border-radius: 12px;\n"
                                              "}\n"
                                              "QFrame:hover{\n"
                                              "    border: 1px solid #3388FF;\n"
                                              "}")
        self.pendingAmountLayout = QVBoxLayout(self.card_pendingAmount)
        self.pendingAmountLayout.setObjectName(u"pendingAmountLayout")
        self.pendingAmountLayout.setContentsMargins(14, 12, 14, 12)
        self.label_pendingAmountTitle = QLabel(self.card_pendingAmount)
        self.label_pendingAmountTitle.setObjectName(u"label_pendingAmountTitle")
        self.label_pendingAmountTitle.setStyleSheet(u"font-size: 13px; color: #666; border: none;")

        self.pendingAmountLayout.addWidget(self.label_pendingAmountTitle)

        self.label_pendingAmountValue = QLabel(self.card_pendingAmount)
        self.label_pendingAmountValue.setObjectName(u"label_pendingAmountValue")
        self.label_pendingAmountValue.setStyleSheet(u"font-size: 22px; font-weight: 800; color: #111; border: none;")

        self.pendingAmountLayout.addWidget(self.label_pendingAmountValue)

        self.cardsLayout.addWidget(self.card_pendingAmount)

        self.mainLayout.addWidget(self.cards_widget)

        self.content_container = QWidget(StudentFeesPage)
        self.content_container.setObjectName(u"content_container")
        self.content_container.setStyleSheet(u"background: transparent;")
        self.contentLayout = QHBoxLayout(self.content_container)
        self.contentLayout.setSpacing(12)
        self.contentLayout.setObjectName(u"contentLayout")
        self.contentLayout.setContentsMargins(0, 0, 0, 0)
        self.history_container = QWidget(self.content_container)
        self.history_container.setObjectName(u"history_container")
        self.history_container.setStyleSheet(u"#history_container{\n"
                                             "background-color: rgb(255, 255, 255);\n"
                                             "border:1px solid rgb(187, 187, 187);\n"
                                             "border-radius: 10px;\n"
                                             "}")
        self.historyLayout = QVBoxLayout(self.history_container)
        self.historyLayout.setSpacing(0)
        self.historyLayout.setObjectName(u"historyLayout")
        self.historyLayout.setContentsMargins(0, 0, 0, 0)
        self.historyHeader = QFrame(self.history_container)
        self.historyHeader.setObjectName(u"historyHeader")
        self.historyHeader.setStyleSheet(u"\n"
                                         "QFrame{border:none}\n"
                                         "QLabel{\n"
                                         "    font-size: 13px;\n"
                                         "    color: #333;\n"
                                         "    font-weight: 700;\n"
                                         "    border:none;\n"
                                         "}\n"
                                         "")
        self.historyHeaderLayout = QHBoxLayout(self.historyHeader)
        self.historyHeaderLayout.setObjectName(u"historyHeaderLayout")
        self.historyHeaderLayout.setContentsMargins(12, 12, 12, 12)
        self.label_historyTitle = QLabel(self.historyHeader)
        self.label_historyTitle.setObjectName(u"label_historyTitle")

        self.historyHeaderLayout.addWidget(self.label_historyTitle)

        self.historySpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.historyHeaderLayout.addItem(self.historySpacer)

        self.btn_refresh = QPushButton(self.historyHeader)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_refresh.setStyleSheet(u"\n"
                                       "#btn_refresh{\n"
                                       "    background: transparent;\n"
                                       "    border:none;\n"
                                       "    color:#3388FF;\n"
                                       "    font-weight:700;\n"
                                       "    font-size: 12px;\n"
                                       "}\n"
                                       "#btn_refresh:hover{color:#0055FF;}\n"
                                       "")

        self.historyHeaderLayout.addWidget(self.btn_refresh)

        self.historyLayout.addWidget(self.historyHeader)

        self.history_scroll = QScrollArea(self.history_container)
        self.history_scroll.setObjectName(u"history_scroll")
        self.history_scroll.setFrameShape(QFrame.Shape.NoFrame)
        self.history_scroll.setWidgetResizable(True)
        self.history_scroll_contents = QWidget()
        self.history_scroll_contents.setObjectName(u"history_scroll_contents")
        self.history_scroll_contents.setGeometry(QRect(0, 0, 868, 363))
        self.history_list_layout = QVBoxLayout(self.history_scroll_contents)
        self.history_list_layout.setSpacing(10)
        self.history_list_layout.setObjectName(u"history_list_layout")
        self.history_list_layout.setContentsMargins(12, 12, 12, 12)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.history_list_layout.addItem(self.verticalSpacer)

        self.history_scroll.setWidget(self.history_scroll_contents)

        self.historyLayout.addWidget(self.history_scroll)

        self.contentLayout.addWidget(self.history_container)

        self.mainLayout.addWidget(self.content_container)

        self.retranslateUi(StudentFeesPage)

        QMetaObject.connectSlotsByName(StudentFeesPage)

    # setupUi

    def retranslateUi(self, StudentFeesPage):
        StudentFeesPage.setWindowTitle(QCoreApplication.translate("StudentFeesPage", u"My Fees", None))
        self.pageTitle.setText(QCoreApplication.translate("StudentFeesPage", u"My Fee Overview", None))
        self.label_totalFeesTitle.setText(QCoreApplication.translate("StudentFeesPage", u"Total Fees", None))
        self.label_totalFeesValue.setText(QCoreApplication.translate("StudentFeesPage", u"\u20b90", None))
        self.label_paidAmountTitle.setText(QCoreApplication.translate("StudentFeesPage", u"Paid Amount", None))
        self.label_paidAmountValue.setText(QCoreApplication.translate("StudentFeesPage", u"\u20b90", None))
        self.label_pendingAmountTitle.setText(QCoreApplication.translate("StudentFeesPage", u"Pending Amount", None))
        self.label_pendingAmountValue.setText(QCoreApplication.translate("StudentFeesPage", u"\u20b90", None))
        self.label_historyTitle.setText(QCoreApplication.translate("StudentFeesPage", u"Payment History", None))
        self.btn_refresh.setText(QCoreApplication.translate("StudentFeesPage", u"Refresh", None))
    # retranslateUi
