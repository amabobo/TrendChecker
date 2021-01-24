# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 20:17:27 2020

@author: miosi
"""
import os, sys
import cv2
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ImageGUI import Ui_Form
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter as tk
import ImageUtil
import GraphUtil
import glob


class MainGUI(QtWidgets.QDialog):
    """
    メインクラス
    """
    # 変数宣言
    filepath = None
    """
    ファイルパス格納用
    """

    files = list()
    """
    ミニ画像のファイルパスリスト
    """

    imageMiniObjList = []
    """
    画像表示用オブジェクト格納用配列(ミニ画像)
    """

    cvImgList = []
    """
    画像切り替え用配列
    """

    def __init__(self, parent=None):
        """
        初期処理
        :param parent:
        """
        super(MainGUI, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 画像表示用オブジェクトを配列に格納
        self.imageMiniObjList = [
                        self.ui.InputImageMini1,
                        self.ui.InputImageMini2,
                        self.ui.InputImageMini3,
                        self.ui.InputImageMini4,
                        self.ui.InputImageMini5
                       ]

        # 初期表示に不要なオブジェクトを非表示
        for imageObj in self.imageMiniObjList:
            imageObj.setVisible(False)
            imageObj.installEventFilter(self)

        self.ui.InputImage.setVisible(False)
        self.ui.OutputImage.setVisible(False)
        self.ui.ExtractionBtn.setVisible(False)

    def eventFilter(self, source, event):
        """
        イベント追加
        :param source:
        :param event:
        :return:
        """
        def scale_box(img, width, height):
            """
            アスペクト比を維持したまま画像サイズ調整
            :param img: 画像データ
            :param width: 高さ
            :param height: 幅
            :return: 調整後画像データ
            """
            h, w = img.shape[:2]
            aspect = w / h
            if width / height >= aspect:
                nh = height
                nw = round(nh * aspect)
            else:
                nw = width
                nh = round(nw / aspect)

            dst = cv2.resize(img, dsize=(nw, nh))

            return dst

        # マウスクリック時イベント
        if event.type() == QEvent.MouseButtonPress:
            if event.button() == Qt.LeftButton:

                pushNum = None
                # 押されたimageによって処理分岐
                if source.objectName() == "InputImageMini1":
                    print("1")
                    pushNum = 0
                elif source.objectName() == "InputImageMini2":
                    print("2")
                    pushNum = 1
                elif source.objectName() == "InputImageMini3":
                    print("3")
                    pushNum = 2
                elif source.objectName() == "InputImageMini4":
                    print("4")
                    pushNum = 3
                elif source.objectName() == "InputImageMini5":
                    print("5")
                    pushNum = 4

                # 画像読み込みとサイズ調整
                cv_img = cv2.cvtColor(self.cvImgList[pushNum], cv2.COLOR_BGR2RGB)
                cv_img = scale_box(cv_img, 440, 340)
                height, width, dim = cv_img.shape
                bytesPerLine = dim * width
                self.scene = QGraphicsScene()
                self.image = QImage(cv_img.data, width, height, bytesPerLine, QImage.Format_RGB888)
                self.item = QGraphicsPixmapItem(QPixmap.fromImage(self.image))
                self.scene.addItem(self.item)
                self.ui.InputImage.setScene(self.scene)

        return QWidget.eventFilter(self, source, event)

    def slot1(self):  # イベント処理の関数
        self.ui.label.setText('Hello World!')

    def showFile(self):
        """
        ファイル選択ボタン押下時処理
        :return: void
        """

        def scale_box(img, width, height):
            """
            アスペクト比を維持したまま画像サイズ調整
            :param img: 画像データ
            :param width: 高さ
            :param height: 幅
            :return: 調整後画像データ
            """
            h, w = img.shape[:2]
            aspect = w / h
            if width / height >= aspect:
                nh = height
                nw = round(nh * aspect)
            else:
                nw = width
                nh = round(nw / aspect)

            dst = cv2.resize(img, dsize=(nw, nh))

            return dst

        root = tk.Tk()
        root.withdraw()

        # ファイル種類のフィルタ指定とファイルパス取得と表示（今回はjpeg)
        fTyp = [("画像ファイル", "*.jpeg"), ("画像ファイル", "*.jpg")]
        iDir = os.path.abspath(os.path.dirname(__file__))

        # 選択したファイルのパスを取得
        self.filepath = filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)

        # ファイル選択指定なし？
        if self.filepath == "":
            return

        # 選択したパス情報を設定
        self.ui.FilePathTxt.setText(self.filepath)

        # 画像読み込みとサイズ調整
        cv_img = cv2.imread(self.filepath)
        cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        # cv_img = cv2.resize(cv_img, dsize=(nw,nh))

        cv_img = scale_box(cv_img, 440, 340)

        height, width, dim = cv_img.shape
        bytesPerLine = dim * width
        self.scene = QGraphicsScene()
        self.image = QImage(cv_img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.item = QGraphicsPixmapItem(QPixmap.fromImage(self.image))
        self.scene.addItem(self.item)
        self.ui.InputImage.setScene(self.scene)
        self.ui.InputImage.setVisible(True)
        self.ui.ExtractionBtn.setVisible(True)

    def showFolder(self):
        """
        フォルダ選択ボタン押下時処理
        :return: void
        """
        
        def scale_box(img, width, height):
            """
            アスペクト比を維持したまま画像サイズ調整
            :param img: 画像データ
            :param width: 高さ
            :param height: 幅
            :return: 調整後画像データ
            """
            h, w = img.shape[:2]
            aspect = w / h
            if width / height >= aspect:
                nh = height
                nw = round(nh * aspect)
            else:
                nw = width
                nh = round(nw / aspect)

            dst = cv2.resize(img, dsize=(nw, nh))

            return dst

        root = tk.Tk()
        root.withdraw()

        iDir = os.path.abspath(os.path.dirname(__file__))

        # 選択したフォルダのパスを取得
        self.filepath = filedialog.askdirectory(initialdir=iDir)

        # ファイル選択指定なし？
        if self.filepath == "":
            return

        # 選択したパス情報を設定
        self.ui.FilePathTxt.setText(self.filepath)

        # 選択したフォルダ内の画像ファイルを取得
        self.files = glob.glob(self.filepath + '/*.jpg')

        # ファイル配列用インデックス
        fileIdx = 0

        # imageMiniObjでループ
        for imageObj in self.imageMiniObjList:

            if not self.files:
                break

            if fileIdx >= len(self.files):
                break

            if fileIdx == 0:

                # 切り替え用配列初期化
                self.cvImgList = []

                # 画像読み込み
                cv_img = cv2.imread(self.files[fileIdx])

                # 切り替え用配列に格納
                self.cvImgList.append(cv_img)

                cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)

                # 最初の一枚のみ、InputImageとImageMini両方に格納
                cv_img = scale_box(cv_img, 440, 340)
                height, width, dim = cv_img.shape
                bytesPerLine = dim * width
                self.scene = QGraphicsScene()
                self.image = QImage(cv_img.data, width, height, bytesPerLine, QImage.Format_RGB888)
                self.item = QGraphicsPixmapItem(QPixmap.fromImage(self.image))
                self.scene.addItem(self.item)
                self.ui.InputImage.setScene(self.scene)
                self.ui.InputImage.setVisible(True)

                cv_img = scale_box(cv_img, 75, 85)
                height, width, dim = cv_img.shape
                bytesPerLine = dim * width
                self.scene = QGraphicsScene()
                self.image = QImage(cv_img.data, width, height, bytesPerLine, QImage.Format_RGB888)
                self.item = QGraphicsPixmapItem(QPixmap.fromImage(self.image))
                self.scene.addItem(self.item)
                imageObj.setScene(self.scene)
                imageObj.setVisible(True)

            else:
                # 画像読み込みとサイズ調整
                cv_img = cv2.imread(self.files[fileIdx])

                # 切り替え用配列に格納
                self.cvImgList.append(cv_img)

                cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
                cv_img = scale_box(cv_img, 75, 85)
                height, width, dim = cv_img.shape
                bytesPerLine = dim * width
                self.scene = QGraphicsScene()
                self.image = QImage(cv_img.data, width, height, bytesPerLine, QImage.Format_RGB888)
                self.item = QGraphicsPixmapItem(QPixmap.fromImage(self.image))
                self.scene.addItem(self.item)
                imageObj.setScene(self.scene)
                imageObj.setVisible(True)

            # インデックスを次に進める
            fileIdx += 1

        self.ui.ExtractionBtn.setVisible(True)

    #########################
    #   抽出ボタンクリック関数   #
    #########################
    def colorExtraction(self):
        
        if not self.files:
            self.files.append(self.filepath)
        
        # 色を取得します。
        dicImageColor = ImageUtil.start(self.files)

        # グラフに出力します。
        GraphUtil.createGraph(dicImageColor)

        # グラフの画像を表示します。
        cv_img = cv2.imread("./img.png")
        cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        cv_img = cv2.resize(cv_img, dsize=(440, 340))
        height, width, dim = cv_img.shape
        bytesPerLine = dim * width
        self.scene = QGraphicsScene()
        self.image = QImage(cv_img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.item = QGraphicsPixmapItem(QPixmap.fromImage(self.image))
        self.scene.addItem(self.item)
        self.ui.OutputImage.setScene(self.scene)
        self.ui.OutputImage.setVisible(True)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainGUI()
    window.show()
    sys.exit(app.exec_())
