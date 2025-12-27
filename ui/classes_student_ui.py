# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'classesStudent.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_classes_student(object):
    def setupUi(self, classes_student):
        if not classes_student.objectName():
            classes_student.setObjectName(u"classes_student")
        classes_student.resize(871, 562)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(classes_student.sizePolicy().hasHeightForWidth())
        classes_student.setSizePolicy(sizePolicy)
        classes_student.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.verticalLayout = QVBoxLayout(classes_student)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(classes_student)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.refresh_classes = QPushButton(self.widget)
        self.refresh_classes.setObjectName(u"refresh_classes")
        self.refresh_classes.setStyleSheet(u"color: rgb(34, 34, 34);\n"
"font: 600 18pt \"Segoe UI\";")

        self.horizontalLayout_2.addWidget(self.refresh_classes)

        self.horizontalSpacer = QSpacerItem(587, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_join_class = QPushButton(self.widget)
        self.btn_join_class.setObjectName(u"btn_join_class")
        self.btn_join_class.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_join_class.setStyleSheet(u"color: #fff;\n"
"background : qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(42, 183, 157), stop:1 #067d68);;\n"
"border: none;\n"
"padding: 10px 20px;\n"
"font: 800 14px \"Segoe UI\";\n"
"border-radius: 7px")
        icon = QIcon()
        icon.addFile(u"../icons/join.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_join_class.setIcon(icon)
        self.btn_join_class.setIconSize(QSize(15, 15))

        self.horizontalLayout_2.addWidget(self.btn_join_class)


        self.verticalLayout.addWidget(self.widget)

        self.classes_stacked = QStackedWidget(classes_student)
        self.classes_stacked.setObjectName(u"classes_stacked")
        self.no_class = QWidget()
        self.no_class.setObjectName(u"no_class")
        self.verticalLayout_5 = QVBoxLayout(self.no_class)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_2 = QWidget(self.no_class)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QLabel{\n"
"  \n"
"  font: 15pt \"Segoe UI\";\n"
"  color: rgb(0, 0, 0);\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)


        self.verticalLayout_5.addWidget(self.widget_2)

        self.classes_stacked.addWidget(self.no_class)
        self.all_class = QWidget()
        self.all_class.setObjectName(u"all_class")
        self.verticalLayout_3 = QVBoxLayout(self.all_class)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.class_list_container = QScrollArea(self.all_class)
        self.class_list_container.setObjectName(u"class_list_container")
        self.class_list_container.setWidgetResizable(True)
        self.class_list_container.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 849, 474))
        self.classesLayout = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.classesLayout.setObjectName(u"classesLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.classesLayout.addItem(self.verticalSpacer)

        self.class_list_container.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_3.addWidget(self.class_list_container)

        self.classes_stacked.addWidget(self.all_class)

        self.verticalLayout.addWidget(self.classes_stacked)


        self.retranslateUi(classes_student)

        self.classes_stacked.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(classes_student)
    # setupUi

    def retranslateUi(self, classes_student):
        classes_student.setWindowTitle(QCoreApplication.translate("classes_student", u"Form", None))
        self.refresh_classes.setText(QCoreApplication.translate("classes_student", u"All Classes", None))
        self.btn_join_class.setText(QCoreApplication.translate("classes_student", u"Join Class", None))
        self.label_2.setText(QCoreApplication.translate("classes_student", u"No Class Joined!", None))
    # retranslateUi

