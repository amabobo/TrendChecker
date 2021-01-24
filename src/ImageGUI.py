# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1104, 546)
        self.InputImage = QtWidgets.QGraphicsView(Form)
        self.InputImage.setEnabled(True)
        self.InputImage.setGeometry(QtCore.QRect(20, 80, 450, 350))
        self.InputImage.setAutoFillBackground(True)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.InputImage.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.InputImage.setForegroundBrush(brush)
        self.InputImage.setObjectName("InputImage")
        self.ReferenceBtn = QtWidgets.QPushButton(Form)
        self.ReferenceBtn.setGeometry(QtCore.QRect(290, 20, 75, 23))
        self.ReferenceBtn.setObjectName("ReferenceBtn")
        self.FilePathTxt = QtWidgets.QLineEdit(Form)
        self.FilePathTxt.setGeometry(QtCore.QRect(20, 20, 251, 20))
        self.FilePathTxt.setObjectName("FilePathTxt")
        self.ExtractionBtn = QtWidgets.QPushButton(Form)
        self.ExtractionBtn.setGeometry(QtCore.QRect(500, 230, 111, 41))
        self.ExtractionBtn.setObjectName("ExtractionBtn")
        self.OutputImage = QtWidgets.QGraphicsView(Form)
        self.OutputImage.setEnabled(True)
        self.OutputImage.setGeometry(QtCore.QRect(640, 80, 450, 350))
        self.OutputImage.setAutoFillBackground(True)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.OutputImage.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.OutputImage.setForegroundBrush(brush)
        self.OutputImage.setObjectName("OutputImage")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 440, 451, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.InputImageMini1 = QtWidgets.QGraphicsView(self.horizontalLayoutWidget)
        self.InputImageMini1.setObjectName("InputImageMini1")
        self.horizontalLayout.addWidget(self.InputImageMini1)
        self.InputImageMini2 = QtWidgets.QGraphicsView(self.horizontalLayoutWidget)
        self.InputImageMini2.setObjectName("InputImageMini2")
        self.horizontalLayout.addWidget(self.InputImageMini2)
        self.InputImageMini3 = QtWidgets.QGraphicsView(self.horizontalLayoutWidget)
        self.InputImageMini3.setObjectName("InputImageMini3")
        self.horizontalLayout.addWidget(self.InputImageMini3)
        self.InputImageMini4 = QtWidgets.QGraphicsView(self.horizontalLayoutWidget)
        self.InputImageMini4.setObjectName("InputImageMini4")
        self.horizontalLayout.addWidget(self.InputImageMini4)
        self.InputImageMini5 = QtWidgets.QGraphicsView(self.horizontalLayoutWidget)
        self.InputImageMini5.setObjectName("InputImageMini5")
        self.horizontalLayout.addWidget(self.InputImageMini5)
        self.ReferenceBtn_2 = QtWidgets.QPushButton(Form)
        self.ReferenceBtn_2.setGeometry(QtCore.QRect(380, 20, 75, 23))
        self.ReferenceBtn_2.setObjectName("ReferenceBtn_2")

        self.retranslateUi(Form)
        self.ReferenceBtn.clicked.connect(Form.showFile)
        self.ExtractionBtn.clicked.connect(Form.colorExtraction)
        self.ReferenceBtn_2.clicked.connect(Form.showFolder)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ReferenceBtn.setText(_translate("Form", "ファイル選択"))
        self.ExtractionBtn.setText(_translate("Form", "抽出"))
        self.ReferenceBtn_2.setText(_translate("Form", "フォルダ選択"))

