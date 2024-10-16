# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboardHlCntj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(732, 481)
        MainWindow.setStyleSheet(u"background-color:black;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.progressBar_2 = QProgressBar(self.centralwidget)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setStyleSheet(u"QProgressBar {\n"
"	\n"
"\n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"     background:yellow;\n"
" }")
        self.progressBar_2.setValue(99)
        self.progressBar_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.progressBar_2.setTextVisible(False)

        self.gridLayout_2.addWidget(self.progressBar_2, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color:yellow;")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.rpm = QLabel(self.centralwidget)
        self.rpm.setObjectName(u"rpm")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(30)
        self.rpm.setFont(font)
        self.rpm.setStyleSheet(u"color:white;")
        self.rpm.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.rpm)

        self.gear = QLabel(self.centralwidget)
        self.gear.setObjectName(u"gear")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(74)
        self.gear.setFont(font1)
        self.gear.setStyleSheet(u"color:yellow; text-align: center;")
        self.gear.setLineWidth(0)
        self.gear.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.gear)

        self.speed = QLabel(self.centralwidget)
        self.speed.setObjectName(u"speed")
        font2 = QFont()
        font2.setPointSize(28)
        self.speed.setFont(font2)
        self.speed.setStyleSheet(u"color:white;")
        self.speed.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.speed)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(16)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color:yellow")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)


        self.gridLayout.addLayout(self.verticalLayout, 3, 3, 1, 1)

        self.line_14 = QFrame(self.centralwidget)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setStyleSheet(u"background:yellow")
        self.line_14.setFrameShape(QFrame.VLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_14, 5, 5, 1, 1)

        self.line_7 = QFrame(self.centralwidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_7, 3, 4, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)

        self.frontRightTemp = QLabel(self.centralwidget)
        self.frontRightTemp.setObjectName(u"frontRightTemp")
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(25)
        self.frontRightTemp.setFont(font4)
        self.frontRightTemp.setStyleSheet(u"color:white;")

        self.gridLayout_3.addWidget(self.frontRightTemp, 1, 2, 1, 1)

        self.rearLeftPressure = QLabel(self.centralwidget)
        self.rearLeftPressure.setObjectName(u"rearLeftPressure")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(15)
        self.rearLeftPressure.setFont(font5)
        self.rearLeftPressure.setStyleSheet(u"color:white;")
        self.rearLeftPressure.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.rearLeftPressure, 4, 0, 1, 1)

        self.frontLeftTemp = QLabel(self.centralwidget)
        self.frontLeftTemp.setObjectName(u"frontLeftTemp")
        self.frontLeftTemp.setFont(font4)
        self.frontLeftTemp.setStyleSheet(u"color:white;")

        self.gridLayout_3.addWidget(self.frontLeftTemp, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.rearLeftTemp = QLabel(self.centralwidget)
        self.rearLeftTemp.setObjectName(u"rearLeftTemp")
        self.rearLeftTemp.setFont(font4)
        self.rearLeftTemp.setStyleSheet(u"color:white;")

        self.gridLayout_3.addWidget(self.rearLeftTemp, 5, 0, 1, 1)

        self.rearRightPressure = QLabel(self.centralwidget)
        self.rearRightPressure.setObjectName(u"rearRightPressure")
        self.rearRightPressure.setFont(font5)
        self.rearRightPressure.setStyleSheet(u"color:white;")
        self.rearRightPressure.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.rearRightPressure, 4, 2, 1, 1)

        self.rearRightTemp = QLabel(self.centralwidget)
        self.rearRightTemp.setObjectName(u"rearRightTemp")
        self.rearRightTemp.setFont(font4)
        self.rearRightTemp.setStyleSheet(u"color:white;")

        self.gridLayout_3.addWidget(self.rearRightTemp, 5, 2, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(14)
        self.label_7.setFont(font6)
        self.label_7.setContextMenuPolicy(Qt.CustomContextMenu)
        self.label_7.setStyleSheet(u"color:white;")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_7, 0, 1, 1, 1)

        self.frontLeftPressure = QLabel(self.centralwidget)
        self.frontLeftPressure.setObjectName(u"frontLeftPressure")
        self.frontLeftPressure.setFont(font5)
        self.frontLeftPressure.setStyleSheet(u"color:white;")
        self.frontLeftPressure.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.frontLeftPressure, 2, 0, 1, 1)

        self.frontRightPressure = QLabel(self.centralwidget)
        self.frontRightPressure.setObjectName(u"frontRightPressure")
        self.frontRightPressure.setFont(font5)
        self.frontRightPressure.setStyleSheet(u"color:white;")
        self.frontRightPressure.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.frontRightPressure, 2, 2, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 3, 6, 1, 1)

        self.line_10 = QFrame(self.centralwidget)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_10, 1, 5, 1, 1)

        self.line_15 = QFrame(self.centralwidget)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setStyleSheet(u"background:yellow")
        self.line_15.setFrameShape(QFrame.VLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_15, 5, 1, 1, 1)

        self.line_11 = QFrame(self.centralwidget)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setStyleSheet(u"background:yellow;")
        self.line_11.setFrameShape(QFrame.VLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_11, 3, 5, 1, 1)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color:yellow;")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 4, 0, 1, 1)

        self.line_9 = QFrame(self.centralwidget)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setStyleSheet(u"background:yellow;")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_9, 3, 1, 1, 1)

        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_6, 1, 4, 1, 1)

        self.line_13 = QFrame(self.centralwidget)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setStyleSheet(u"b")
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_13, 2, 3, 1, 1)

        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setFont(font6)
        self.textEdit_2.setStyleSheet(u"color:white; border: 1px solid white;")
        self.textEdit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setAcceptRichText(True)

        self.gridLayout.addWidget(self.textEdit_2, 1, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(11)
        self.label_9.setFont(font7)
        self.label_9.setStyleSheet(u"color:white;")

        self.verticalLayout_4.addWidget(self.label_9)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font7)
        self.label_10.setStyleSheet(u"color:white;")

        self.verticalLayout_4.addWidget(self.label_10)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font7)
        self.label_11.setStyleSheet(u"color:white;")

        self.verticalLayout_4.addWidget(self.label_11)


        self.gridLayout.addLayout(self.verticalLayout_4, 5, 0, 1, 1)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"c")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_5, 1, 1, 1, 1)

        self.line_12 = QFrame(self.centralwidget)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.VLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_12, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 3, 1, 1)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFont(font6)
        self.textEdit.setStyleSheet(u"color:white; border: 1px solid white;")
        self.textEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit, 1, 6, 1, 1)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"background-color:yellow;")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_4, 2, 0, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background:yellow;")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 4, 6, 1, 1)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"background-color:yellow;")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 2, 6, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.progressBar_3 = QProgressBar(self.centralwidget)
        self.progressBar_3.setObjectName(u"progressBar_3")
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(10)
        self.progressBar_3.setFont(font8)
        self.progressBar_3.setStyleSheet(u"QProgressBar {\n"
"	 border:1px solid lightgreen;\n"
"     color:purple;\n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"     background-color: #00FF00;\n"
" }")
        self.progressBar_3.setValue(50)
        self.progressBar_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.progressBar_3)

        self.progressBar_4 = QProgressBar(self.centralwidget)
        self.progressBar_4.setObjectName(u"progressBar_4")
        self.progressBar_4.setFont(font8)
        self.progressBar_4.setStyleSheet(u"QProgressBar {\n"
"	 border:1px solid red;\n"
"     color:white;\n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"     background-color: red;\n"
" }\n"
"")
        self.progressBar_4.setValue(24)
        self.progressBar_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.progressBar_4)


        self.gridLayout.addLayout(self.verticalLayout_3, 5, 6, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(3)
        self.gridLayout_4.setVerticalSpacing(0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.current_mpg = QLabel(self.centralwidget)
        self.current_mpg.setObjectName(u"current_mpg")
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(12)
        self.current_mpg.setFont(font9)
        self.current_mpg.setStyleSheet(u"color:white;")
        self.current_mpg.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.current_mpg)

        self.ethanol = QLabel(self.centralwidget)
        self.ethanol.setObjectName(u"ethanol")
        self.ethanol.setFont(font9)
        self.ethanol.setStyleSheet(u"color:white;")
        self.ethanol.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ethanol)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)


        self.gridLayout_4.addLayout(self.verticalLayout_2, 1, 2, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font10 = QFont()
        font10.setFamily(u"Segoe UI")
        font10.setPointSize(13)
        self.label.setFont(font10)
        self.label.setStyleSheet(u"color:white;")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label, 0, 1, 1, 1)

        self.line_8 = QFrame(self.centralwidget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_8, 1, 4, 1, 1)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	 border:1px solid white;\n"
"\n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"     background-color: white;\n"
" } color:white;")
        self.progressBar.setValue(25)
        self.progressBar.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Vertical)

        self.gridLayout_4.addWidget(self.progressBar, 1, 0, 1, 1)

        self.progressBar_5 = QProgressBar(self.centralwidget)
        self.progressBar_5.setObjectName(u"progressBar_5")
        self.progressBar_5.setStyleSheet(u"QProgressBar {\n"
"	 border:1px solid white;\n"
"\n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"     background-color: #90EE90;\n"
" } color:white;")
        self.progressBar_5.setValue(100)
        self.progressBar_5.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.progressBar_5.setTextVisible(True)
        self.progressBar_5.setOrientation(Qt.Vertical)
        self.progressBar_5.setTextDirection(QProgressBar.TopToBottom)

        self.gridLayout_4.addWidget(self.progressBar_5, 1, 3, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font10)
        self.label_8.setStyleSheet(u"color:white; ")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_8, 0, 2, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.fuel_left = QLabel(self.centralwidget)
        self.fuel_left.setObjectName(u"fuel_left")
        self.fuel_left.setFont(font9)
        self.fuel_left.setStyleSheet(u"color:white;")
        self.fuel_left.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.fuel_left)

        self.range_laps = QLabel(self.centralwidget)
        self.range_laps.setObjectName(u"range_laps")
        self.range_laps.setFont(font9)
        self.range_laps.setStyleSheet(u"color:white;")
        self.range_laps.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.range_laps)

        self.range = QLabel(self.centralwidget)
        self.range.setObjectName(u"range")
        self.range.setFont(font9)
        self.range.setStyleSheet(u"color:white;")
        self.range.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.range)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_2)


        self.gridLayout_4.addLayout(self.verticalLayout_6, 1, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_4, 3, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setFont(font6)
        self.plainTextEdit.setStyleSheet(u"color:white; border: 1px solid white;")
        self.plainTextEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.plainTextEdit, 5, 3, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.progressBar_2.setFormat(QCoreApplication.translate("MainWindow", u"%pk rpm", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"RPM", None))
        self.rpm.setText(QCoreApplication.translate("MainWindow", u"0000", None))
        self.gear.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.speed.setText(QCoreApplication.translate("MainWindow", u"000", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SPEED", None))
        self.frontRightTemp.setText(QCoreApplication.translate("MainWindow", u"30C", None))
        self.rearLeftPressure.setText(QCoreApplication.translate("MainWindow", u"27psi", None))
        self.frontLeftTemp.setText(QCoreApplication.translate("MainWindow", u"30C", None))
        self.rearLeftTemp.setText(QCoreApplication.translate("MainWindow", u"30C", None))
        self.rearRightPressure.setText(QCoreApplication.translate("MainWindow", u"27psi", None))
        self.rearRightTemp.setText(QCoreApplication.translate("MainWindow", u"30C", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Tires", None))
        self.frontLeftPressure.setText(QCoreApplication.translate("MainWindow", u"27psi", None))
        self.frontRightPressure.setText(QCoreApplication.translate("MainWindow", u"27psi", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">LOW FUEL</p></body></html>", None))
        self.textEdit_2.setPlaceholderText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Coolant Temp 80C", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Oil Temp 100C", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Air Temp 31C", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.current_mpg.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.ethanol.setText(QCoreApplication.translate("MainWindow", u"Hotlap", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Fuel", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Battery", None))
        self.fuel_left.setText(QCoreApplication.translate("MainWindow", u"5 Liters", None))
        self.range_laps.setText(QCoreApplication.translate("MainWindow", u"1.2 laps", None))
        self.range.setText(QCoreApplication.translate("MainWindow", u"10km", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.plainTextEdit.setPlainText("")
    # retranslateUi

