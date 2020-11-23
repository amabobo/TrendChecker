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
        Form.resize(1104, 483)
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
        self.ReferenceBtn.setGeometry(QtCore.QRect(530, 20, 75, 23))
        self.ReferenceBtn.setObjectName("ReferenceBtn")
        self.FilePathTxt = QtWidgets.QLineEdit(Form)
        self.FilePathTxt.setGeometry(QtCore.QRect(20, 20, 491, 20))
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

        self.retranslateUi(Form)
        self.ReferenceBtn.clicked.connect(Form.showFolder)
        self.ExtractionBtn.clicked.connect(Form.colorExtraction)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ReferenceBtn.setText(_translate("Form", "参照"))
        self.ExtractionBtn.setText(_translate("Form", "抽出"))

