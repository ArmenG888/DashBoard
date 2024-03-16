# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'porschedashboardvUEEqz.ui'
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
        MainWindow.resize(800, 480)
        MainWindow.setStyleSheet(u"background-color:#05070B;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 70, 801, 301))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 7, -1, -1)
        self.label_15 = QLabel(self.horizontalLayoutWidget)
        self.label_15.setObjectName(u"label_15")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(24)
        self.label_15.setFont(font)

        self.verticalLayout_9.addWidget(self.label_15)


        self.verticalLayout_4.addLayout(self.verticalLayout_9)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_16 = QLabel(self.horizontalLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(12)
        self.label_16.setFont(font1)
        self.label_16.setStyleSheet(u"color:white; background-color:#19353C;")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_16)

        self.fuel_used = QLabel(self.horizontalLayoutWidget)
        self.fuel_used.setObjectName(u"fuel_used")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(14)
        self.fuel_used.setFont(font2)
        self.fuel_used.setCursor(QCursor(Qt.CrossCursor))
        self.fuel_used.setStyleSheet(u"border-right:3px solid #19353C; color:white; border-top:3px solid #19353C")
        self.fuel_used.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.fuel_used)


        self.verticalLayout_13.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_19 = QLabel(self.horizontalLayoutWidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)
        self.label_19.setStyleSheet(u"color:white; background-color:#19353C;")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_19)

        self.fuelperlap = QLabel(self.horizontalLayoutWidget)
        self.fuelperlap.setObjectName(u"fuelperlap")
        self.fuelperlap.setFont(font2)
        self.fuelperlap.setCursor(QCursor(Qt.CrossCursor))
        self.fuelperlap.setStyleSheet(u"border-right:3px solid #19353C; color:white;")
        self.fuelperlap.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.fuelperlap)


        self.verticalLayout_13.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_20 = QLabel(self.horizontalLayoutWidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)
        self.label_20.setStyleSheet(u"color:white; background-color:#19353C;")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_20)

        self.fuelpress = QLabel(self.horizontalLayoutWidget)
        self.fuelpress.setObjectName(u"fuelpress")
        self.fuelpress.setFont(font2)
        self.fuelpress.setCursor(QCursor(Qt.CrossCursor))
        self.fuelpress.setStyleSheet(u"border-right:3px solid #19353C; color:white;")
        self.fuelpress.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.fuelpress)


        self.verticalLayout_13.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_22 = QLabel(self.horizontalLayoutWidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)
        self.label_22.setStyleSheet(u"color:white; background-color:#19353C;")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_22)

        self.fuel_level = QLabel(self.horizontalLayoutWidget)
        self.fuel_level.setObjectName(u"fuel_level")
        self.fuel_level.setFont(font2)
        self.fuel_level.setCursor(QCursor(Qt.CrossCursor))
        self.fuel_level.setStyleSheet(u"border-right:3px solid #19353C; color:white; border-bottom:3px solid  #19353C")
        self.fuel_level.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.fuel_level)


        self.verticalLayout_13.addLayout(self.horizontalLayout_14)


        self.verticalLayout_4.addLayout(self.verticalLayout_13)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tc = QLabel(self.horizontalLayoutWidget)
        self.tc.setObjectName(u"tc")
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.tc.setFont(font3)
        self.tc.setStyleSheet(u"color:white; border: 2px solid red; border-radius:5px;")
        self.tc.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.tc)

        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color:white; border: 2px solid green; border-radius:5px;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout_15.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_4)

        self.abs = QLabel(self.horizontalLayoutWidget)
        self.abs.setObjectName(u"abs")
        self.abs.setFont(font3)
        self.abs.setStyleSheet(u"color:white; border: 2px solid blue; border-radius:5px;\n"
"padding-left:10px;\n"
"padding-right:10px;")
        self.abs.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.abs)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 2)
        self.horizontalLayout_11.setStretch(2, 1)

        self.verticalLayout_15.addLayout(self.horizontalLayout_11)


        self.verticalLayout_4.addLayout(self.verticalLayout_15)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 10)
        self.verticalLayout_4.setStretch(2, 6)

        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, 0, -1, -1)
        self.speed = QLabel(self.horizontalLayoutWidget)
        self.speed.setObjectName(u"speed")
        self.speed.setFont(font)
        self.speed.setStyleSheet(u"color:white; border:3px solid #19353C; border-radius:5px;")
        self.speed.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.speed)


        self.verticalLayout_6.addLayout(self.verticalLayout_16)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(-1, 0, -1, -1)
        self.gear = QLabel(self.horizontalLayoutWidget)
        self.gear.setObjectName(u"gear")
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(68)
        self.gear.setFont(font4)
        self.gear.setStyleSheet(u"color:white; border:3px solid #19353C;border-radius:5px;")
        self.gear.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.gear)


        self.verticalLayout_6.addLayout(self.verticalLayout_18)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color:white; background-color:#D4891A;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.front_left = QLabel(self.horizontalLayoutWidget)
        self.front_left.setObjectName(u"front_left")
        self.front_left.setFont(font2)
        self.front_left.setStyleSheet(u"color:white; border-left: 3px solid #D4891A;")
        self.front_left.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.front_left)

        self.front_right = QLabel(self.horizontalLayoutWidget)
        self.front_right.setObjectName(u"front_right")
        self.front_right.setFont(font2)
        self.front_right.setStyleSheet(u"color:white; border-right: 3px solid #D4891A;")
        self.front_right.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.front_right)


        self.verticalLayout_8.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.rear_left = QLabel(self.horizontalLayoutWidget)
        self.rear_left.setObjectName(u"rear_left")
        self.rear_left.setFont(font2)
        self.rear_left.setStyleSheet(u"color:white; border-left: 3px solid #D4891A; border-bottom: 3px solid #D4891A; ")
        self.rear_left.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.rear_left)

        self.rear_right = QLabel(self.horizontalLayoutWidget)
        self.rear_right.setObjectName(u"rear_right")
        self.rear_right.setFont(font2)
        self.rear_right.setStyleSheet(u"color:white; border-right: 3px solid #D4891A; border-bottom: 3px solid #D4891A;")
        self.rear_right.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.rear_right)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 5)
        self.verticalLayout_8.setStretch(2, 5)

        self.horizontalLayout_2.addLayout(self.verticalLayout_8)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 10)
        self.verticalLayout_6.setStretch(2, 6)

        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 7, -1, -1)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(16)
        self.label.setFont(font5)
        self.label.setStyleSheet(u"color:white;background-color:#19353C; border-radius:5px;\n"
"border-bottom-right-radius:0px;\n"
"border-top-right-radius:0px;\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label)

        self.lap_num = QLabel(self.horizontalLayoutWidget)
        self.lap_num.setObjectName(u"lap_num")
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(13)
        self.lap_num.setFont(font6)
        self.lap_num.setStyleSheet(u"\n"
"\n"
"color:white; border:3px solid #19353C; border-radius:5px;\n"
"border-top-left-radius:0px;\n"
"border-bottom-left-radius:0px;\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"")
        self.lap_num.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lap_num)

        self.horizontalSpacer_2 = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.label_6 = QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_5.addWidget(self.label_6)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_9 = QLabel(self.horizontalLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"color:white; background-color:#19353C;")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_9)


        self.verticalLayout_12.addLayout(self.horizontalLayout_3)

        self.current_laptime = QLabel(self.horizontalLayoutWidget)
        self.current_laptime.setObjectName(u"current_laptime")
        self.current_laptime.setFont(font)
        self.current_laptime.setStyleSheet(u"color:white; border-left:3px solid #19353C;  border-right:3px solid #19353C;")
        self.current_laptime.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.current_laptime)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_11 = QLabel(self.horizontalLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"color:white;background-color:#19353C;")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_11)

        self.label_12 = QLabel(self.horizontalLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"color:white;background-color:#19353C;")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_12)


        self.verticalLayout_12.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.delta = QLabel(self.horizontalLayoutWidget)
        self.delta.setObjectName(u"delta")
        self.delta.setFont(font5)
        self.delta.setStyleSheet(u"color:white; border:3px solid #19353C;")
        self.delta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.delta)

        self.prediction = QLabel(self.horizontalLayoutWidget)
        self.prediction.setObjectName(u"prediction")
        self.prediction.setFont(font5)
        self.prediction.setStyleSheet(u"color:white; border:3px solid #19353C;")
        self.prediction.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.prediction)


        self.verticalLayout_12.addLayout(self.horizontalLayout_7)

        self.verticalLayout_12.setStretch(0, 1)
        self.verticalLayout_12.setStretch(1, 5)
        self.verticalLayout_12.setStretch(2, 1)
        self.verticalLayout_12.setStretch(3, 3)

        self.verticalLayout_5.addLayout(self.verticalLayout_12)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_2)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_24 = QLabel(self.horizontalLayoutWidget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font5)
        self.label_24.setStyleSheet(u"color:white;background-color:#19353C; border-radius:5px;\n"
"border-bottom-right-radius:0px;\n"
"border-top-right-radius:0px;\n"
"")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_24)

        self.brake_bias = QLabel(self.horizontalLayoutWidget)
        self.brake_bias.setObjectName(u"brake_bias")
        self.brake_bias.setFont(font5)
        self.brake_bias.setStyleSheet(u"\n"
"\n"
"color:white; border:3px solid #19353C; border-radius:5px;\n"
"border-top-left-radius:0px;\n"
"border-bottom-left-radius:0px;\n"
"text-align:center;")
        self.brake_bias.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.brake_bias)


        self.verticalLayout_11.addLayout(self.horizontalLayout_15)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer)


        self.verticalLayout_5.addLayout(self.verticalLayout_11)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(2, 10)
        self.verticalLayout_5.setStretch(3, 6)

        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color:white; border:2px solid #157492; border-radius:3px;\n"
"")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_5)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(2, 3)
        self.horizontalLayout.setStretch(3, 4)
        self.horizontalLayout.setStretch(4, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Fuel Used", None))
        self.fuel_used.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Fuel P. Lap", None))
        self.fuelperlap.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Fuel Press", None))
        self.fuelpress.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Fuel Level", None))
        self.fuel_level.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.tc.setText(QCoreApplication.translate("MainWindow", u"TC-LA 4", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TC-LO 0", None))
        self.abs.setText(QCoreApplication.translate("MainWindow", u"ABS 4", None))
        self.speed.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.gear.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TIRE PRESS", None))
        self.front_left.setText(QCoreApplication.translate("MainWindow", u"21.49", None))
        self.front_right.setText(QCoreApplication.translate("MainWindow", u"21.49", None))
        self.rear_left.setText(QCoreApplication.translate("MainWindow", u"21.49", None))
        self.rear_right.setText(QCoreApplication.translate("MainWindow", u"21.49", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Lap", None))
        self.lap_num.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Laptime", None))
        self.current_laptime.setText(QCoreApplication.translate("MainWindow", u"0:00:00", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Time. Diff", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Pred. Time", None))
        self.delta.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.prediction.setText(QCoreApplication.translate("MainWindow", u"0:00:00", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Brakes Bias", None))
        self.brake_bias.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"DRY", None))
    # retranslateUi

