# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(428, 585)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ringBTN = QtWidgets.QToolButton(self.centralwidget)
        self.ringBTN.setGeometry(QtCore.QRect(30, 180, 141, 151))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.ringBTN.sizePolicy().hasHeightForWidth())
        self.ringBTN.setSizePolicy(sizePolicy)
        self.ringBTN.setSizeIncrement(QtCore.QSize(10, 20))
        self.ringBTN.setBaseSize(QtCore.QSize(10, 20))
        self.ringBTN.setStyleSheet("background-image: url(:/newPrefix/Ekran Resmi 2022-11-29 18.32.36.png);")
        self.ringBTN.setText("")
        self.ringBTN.setObjectName("ringBTN")
        self.takvimBTN = QtWidgets.QToolButton(self.centralwidget)
        self.takvimBTN.setGeometry(QtCore.QRect(30, 360, 161, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.takvimBTN.sizePolicy().hasHeightForWidth())
        self.takvimBTN.setSizePolicy(sizePolicy)
        self.takvimBTN.setSizeIncrement(QtCore.QSize(10, 20))
        self.takvimBTN.setBaseSize(QtCore.QSize(10, 20))
        self.takvimBTN.setStyleSheet("background-image: url(:/newPrefix/Ekran Resmi 2022-11-29 18.58.39.png);")
        self.takvimBTN.setText("")
        self.takvimBTN.setObjectName("takvimBTN")
        self.haritaBTN = QtWidgets.QToolButton(self.centralwidget)
        self.haritaBTN.setGeometry(QtCore.QRect(230, 370, 121, 121))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.haritaBTN.sizePolicy().hasHeightForWidth())
        self.haritaBTN.setSizePolicy(sizePolicy)
        self.haritaBTN.setSizeIncrement(QtCore.QSize(10, 20))
        self.haritaBTN.setBaseSize(QtCore.QSize(10, 20))
        self.haritaBTN.setStyleSheet("background-image: url(:/newPrefix/Ekran Resmi 2022-11-29 19.02.51.png);")
        self.haritaBTN.setText("")
        self.haritaBTN.setObjectName("haritaBTN")
        self.yemekhaneBTN = QtWidgets.QToolButton(self.centralwidget)
        self.yemekhaneBTN.setGeometry(QtCore.QRect(110, 40, 201, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.yemekhaneBTN.sizePolicy().hasHeightForWidth())
        self.yemekhaneBTN.setSizePolicy(sizePolicy)
        self.yemekhaneBTN.setSizeIncrement(QtCore.QSize(10, 20))
        self.yemekhaneBTN.setBaseSize(QtCore.QSize(10, 20))
        self.yemekhaneBTN.setStyleSheet("background-image: url(:/newPrefix/Ekran Resmi 2022-11-29 19.11.35.png);")
        self.yemekhaneBTN.setText("")
        self.yemekhaneBTN.setObjectName("yemekhaneBTN")
        self.gpaBTN = QtWidgets.QToolButton(self.centralwidget)
        self.gpaBTN.setGeometry(QtCore.QRect(240, 180, 121, 131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.gpaBTN.sizePolicy().hasHeightForWidth())
        self.gpaBTN.setSizePolicy(sizePolicy)
        self.gpaBTN.setSizeIncrement(QtCore.QSize(10, 20))
        self.gpaBTN.setBaseSize(QtCore.QSize(10, 20))
        self.gpaBTN.setStyleSheet("background-image: url(:/newPrefix/Ekran Resmi 2022-11-29 19.05.14.png);")
        self.gpaBTN.setText("")
        self.gpaBTN.setObjectName("gpaBTN")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 428, 24))
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

import rcs_1