# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TCProgressView.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmProgressView(object):
    def setupUi(self, frmProgressView):
        frmProgressView.setObjectName("frmProgressView")
        frmProgressView.setWindowModality(QtCore.Qt.NonModal)
        frmProgressView.resize(434, 129)
        frmProgressView.setMinimumSize(QtCore.QSize(434, 129))
        frmProgressView.setMaximumSize(QtCore.QSize(434, 213))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        frmProgressView.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon/graph1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmProgressView.setWindowIcon(icon)
        frmProgressView.setAutoFillBackground(False)
        frmProgressView.setStyleSheet("background-color : rgb(255, 255, 255)")
        self.lblLoad = QtWidgets.QLabel(frmProgressView)
        self.lblLoad.setGeometry(QtCore.QRect(180, 50, 64, 64))
        self.lblLoad.setText("")
        self.lblLoad.setObjectName("lblLoad")
        self.pgbGraph = QtWidgets.QProgressBar(frmProgressView)
        self.pgbGraph.setGeometry(QtCore.QRect(20, 20, 401, 21))
        self.pgbGraph.setProperty("value", 0)
        self.pgbGraph.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.pgbGraph.setObjectName("pgbGraph")

        self.retranslateUi(frmProgressView)
        QtCore.QMetaObject.connectSlotsByName(frmProgressView)

    def retranslateUi(self, frmProgressView):
        _translate = QtCore.QCoreApplication.translate
        frmProgressView.setWindowTitle(_translate("frmProgressView", "TrendChecker - Progress"))

