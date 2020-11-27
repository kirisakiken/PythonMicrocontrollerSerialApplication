# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Info(object):
    def setupUi(self, Info):
        Info.setObjectName("Info")
        Info.resize(251, 250)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Info.sizePolicy().hasHeightForWidth())
        Info.setSizePolicy(sizePolicy)
        Info.setMinimumSize(QtCore.QSize(251, 250))
        Info.setMaximumSize(QtCore.QSize(251, 250))
        self.centralwidget = QtWidgets.QWidget(Info)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 221, 241))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        Info.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Info)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 251, 21))
        self.menubar.setObjectName("menubar")
        Info.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Info)
        self.statusbar.setObjectName("statusbar")
        Info.setStatusBar(self.statusbar)

        self.retranslateUi(Info)
        QtCore.QMetaObject.connectSlotsByName(Info)

    def retranslateUi(self, Info):
        _translate = QtCore.QCoreApplication.translate
        Info.setWindowTitle(_translate("Info", "Credits"))
        self.label.setText(_translate("Info", "<html><head/><body><p>Isparta University of</p><p>Applied Sciences</p><p>Mechatronics Engineering Department</p><p>Python Serial Application</p><p><span style=\" font-weight:600; text-decoration: underline;\">CREDITS</span></p><p>Bezmican Zehir</p><p>Şafak Turan</p><p>Mehmet Yelten</p></body></html>"))

