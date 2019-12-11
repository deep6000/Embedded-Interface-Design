# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serverGUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1613, 878)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_img = QtWidgets.QFrame(self.centralwidget)
        self.frame_img.setGeometry(QtCore.QRect(460, 10, 551, 401))
        self.frame_img.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_img.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_img.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_img.setObjectName("frame_img")
        self.label_rw = QtWidgets.QLabel(self.centralwidget)
        self.label_rw.setGeometry(QtCore.QRect(1150, 200, 131, 21))
        self.label_rw.setStyleSheet("border-color: rgb(16, 16, 16);\n"
"font: 75 14pt \"Carlito\";\n"
"color: rgb(32, 170, 255);")
        self.label_rw.setObjectName("label_rw")
        self.label_recog = QtWidgets.QLabel(self.centralwidget)
        self.label_recog.setGeometry(QtCore.QRect(1150, 160, 131, 21))
        self.label_recog.setStyleSheet("border-color: rgb(16, 16, 16);\n"
"font: 75 14pt \"Carlito\";\n"
"color: rgb(32, 170, 255);")
        self.label_recog.setObjectName("label_recog")
        self.push_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.push_refresh.setGeometry(QtCore.QRect(190, 210, 99, 30))
        self.push_refresh.setObjectName("push_refresh")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(460, 540, 541, 261))
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(169)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(46)
        self.push_stats = QtWidgets.QPushButton(self.centralwidget)
        self.push_stats.setGeometry(QtCore.QRect(148, 640, 131, 30))
        self.push_stats.setObjectName("push_stats")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1090, 550, 291, 71))
        self.label_4.setStyleSheet("border-color: rgb(16, 16, 16);\n"
"font: 75 14pt \"Carlito\";\n"
"color: rgb(32, 170, 255);")
        self.label_4.setObjectName("label_4")
        self.label_cmd = QtWidgets.QLabel(self.centralwidget)
        self.label_cmd.setGeometry(QtCore.QRect(1430, 610, 131, 21))
        self.label_cmd.setStyleSheet("border-color: rgb(16, 16, 16);\n"
"font: 75 14pt \"Carlito\";\n"
"color: rgb(32, 170, 255);")
        self.label_cmd.setObjectName("label_cmd")
        self.label_obj = QtWidgets.QLabel(self.centralwidget)
        self.label_obj.setGeometry(QtCore.QRect(1400, 570, 131, 21))
        self.label_obj.setStyleSheet("border-color: rgb(16, 16, 16);\n"
"font: 75 14pt \"Carlito\";\n"
"color: rgb(32, 170, 255);")
        self.label_obj.setObjectName("label_obj")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1090, 590, 321, 71))
        self.label_7.setStyleSheet("border-color: rgb(16, 16, 16);\n"
"font: 75 14pt \"Carlito\";\n"
"color: rgb(32, 170, 255);")
        self.label_7.setObjectName("label_7")
        self.push_close = QtWidgets.QPushButton(self.centralwidget)
        self.push_close.setGeometry(QtCore.QRect(1550, -10, 51, 30))
        self.push_close.setObjectName("push_close")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1613, 28))
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
        self.label_rw.setText(_translate("MainWindow", "TextLabel"))
        self.label_recog.setText(_translate("MainWindow", "TextLabel"))
        self.push_refresh.setText(_translate("MainWindow", "REFRESH"))
        self.push_stats.setText(_translate("MainWindow", "GET STATISTICS"))
        self.label_4.setText(_translate("MainWindow", "% OF OBJECTS DETECTED CORRECTLY"))
        self.label_cmd.setText(_translate("MainWindow", "TextLabel"))
        self.label_obj.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "% OF COMMANDS DETECTED CORRECTLY"))
        self.push_close.setText(_translate("MainWindow", "x"))

