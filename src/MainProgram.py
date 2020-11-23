# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 20:17:27 2020

@author: miosi
"""
import os,sys
import cv2  
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ImageGUI import Ui_Form
from tkinter import filedialog
from PIL import Image, ImageTk  
import tkinter as tk
import ImageUtil
import GraphUtil

class MainGUI(QtWidgets.QDialog):
    
  # 変数  
  filepath = None  
    
  def __init__(self,parent=None):
    super(MainGUI, self).__init__(parent)
    self.ui = Ui_Form()
    self.ui.setupUi(self)
    
    #初期表示に不要なオブジェクトを非表示
    self.ui.InputImage.setVisible(False)
    self.ui.OutputImage.setVisible(False)
    self.ui.ExtractionBtn.setVisible(False)
    
  def slot1(self): #イベント処理の関数
    self.ui.label.setText('Hello World!')

  #########################  
  #   参照ボタンクリック関数   #  
  #########################  
  def showFolder(self):
      
      root=tk.Tk()
      root.withdraw()
      
      # ファイル種類のフィルタ指定とファイルパス取得と表示（今回はjpeg)  
      fTyp = [("画像ファイル","*.jpeg"),("画像ファイル","*.jpg")]  
      iDir = os.path.abspath(os.path.dirname(__file__))  
      
      # 選択したファイルのパスを取得  
      self.filepath = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)  
      
      # ファイル選択指定なし？  
      if self.filepath == "":  
          return  
      
      # 選択したパス情報を設定      
      self.ui.FilePathTxt.setText(self.filepath)
      
      #画像読み込みとサイズ調整
      cv_img = cv2.imread(self.filepath)   
      cv_img = cv2.cvtColor(cv_img,cv2.COLOR_BGR2RGB)
      cv_img = cv2.resize(cv_img,dsize=(440,340))  
      height, width, dim = cv_img.shape
      bytesPerLine = dim * width
      self.scene = QGraphicsScene()
      self.image = QImage(cv_img.data, width, height, bytesPerLine, QImage.Format_RGB888)
      self.item = QGraphicsPixmapItem(QPixmap.fromImage(self.image))
      self.scene.addItem(self.item)
      self.ui.InputImage.setScene(self.scene)
      self.ui.InputImage.setVisible(True)
      self.ui.ExtractionBtn.setVisible(True)

  #########################  
  #   抽出ボタンクリック関数   #  
  ######################### 
  def colorExtraction(self):
      
    # 色を取得します。
    dicImageColor = ImageUtil.start(self.ui.FilePathTxt.text())
    
    # グラフに出力します。
    GraphUtil.createGraph(dicImageColor)
    
if __name__ == '__main__':
  app = QtWidgets.QApplication(sys.argv)
  window = MainGUI()
  window.show()
  sys.exit(app.exec_())