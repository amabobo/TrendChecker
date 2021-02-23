# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TCGraphView.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmGraphView(object):
    def setupUi(self, frmGraphView):
        frmGraphView.setObjectName("frmGraphView")
        frmGraphView.resize(430, 370)
        frmGraphView.setMinimumSize(QtCore.QSize(430, 370))
        frmGraphView.setMaximumSize(QtCore.QSize(430, 370))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        frmGraphView.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon/graph1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmGraphView.setWindowIcon(icon)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(frmGraphView)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 50, 411, 311))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        self.horizontalLayoutWidget_2.setFont(font)
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.mainGraphLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.mainGraphLayout.setContentsMargins(0, 0, 0, 0)
        self.mainGraphLayout.setObjectName("mainGraphLayout")
        self.viewGraphImage = QtWidgets.QGraphicsView(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        self.viewGraphImage.setFont(font)
        self.viewGraphImage.setObjectName("viewGraphImage")
        self.mainGraphLayout.addWidget(self.viewGraphImage)
        self.btnBack = QtWidgets.QPushButton(frmGraphView)
        self.btnBack.setGeometry(QtCore.QRect(10, 10, 75, 27))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnBack.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon1)
        self.btnBack.setObjectName("btnBack")

        self.retranslateUi(frmGraphView)
        self.btnBack.clicked.connect(frmGraphView.back_click)
        QtCore.QMetaObject.connectSlotsByName(frmGraphView)

    def retranslateUi(self, frmGraphView):
        _translate = QtCore.QCoreApplication.translate
        frmGraphView.setWindowTitle(_translate("frmGraphView", "TrendChecker - Graph"))
        self.btnBack.setText(_translate("frmGraphView", "戻る"))

