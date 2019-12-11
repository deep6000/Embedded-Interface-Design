# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clientGUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(70, 80, 651, 411))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lcdNumber_recog = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber_recog.setGeometry(QtCore.QRect(90, 280, 251, 31))
        self.lcdNumber_recog.setObjectName("lcdNumber_recog")
        self.pushButton_close = QtWidgets.QPushButton(self.frame)
        self.pushButton_close.setGeometry(QtCore.QRect(580, 10, 61, 30))
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_mic = QtWidgets.QPushButton(self.frame)
        self.pushButton_mic.setGeometry(QtCore.QRect(520, 170, 20, 21))
        self.pushButton_mic.setStyleSheet("QPushButton {\n"
" \n"
"    color: rgb(170, 0, 0);\n"
"    border: 2px solid #555;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    background-color: rgb(184, 52, 7);\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButton_mic.setText("")
        self.pushButton_mic.setObjectName("pushButton_mic")
        self.label_turn_on_mic = QtWidgets.QLabel(self.frame)
        self.label_turn_on_mic.setGeometry(QtCore.QRect(550, 171, 51, 31))
        self.label_turn_on_mic.setStyleSheet("font: 10pt \"Noto Serif Tibetan\";")
        self.label_turn_on_mic.setObjectName("label_turn_on_mic")
        self.label_img = QtWidgets.QLabel(self.frame)
        self.label_img.setGeometry(QtCore.QRect(100, 40, 331, 211))
        self.label_img.setFrameShape(QtWidgets.QFrame.Box)
        self.label_img.setPixmap(QtGui.QPixmap("image.jpg"))
        self.label_img.setObjectName("label_img")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 40, 161, 41))
        self.label_2.setStyleSheet("font: 12pt \"Bitstream Vera Sans\";")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_close.setText(_translate("MainWindow", "X"))
        self.label_turn_on_mic.setText(_translate("MainWindow", "Mic"))
        self.label_2.setText(_translate("MainWindow", "THE MAGIC  WAND"))

import magicwand_rc
