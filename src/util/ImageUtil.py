import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class ImageUtil:
    """
    画像操作クラス
    """

    def create_scene(self, file_path, view_height, view_width):
        """
        画像表示用のシーンを生成する
        :param file_path: ファイルパス
        :param view_height: 表示領域の高さ
        :param view_width: 表示領域の幅
        :return: 表示用シーン
        """

        # 画像読み込み
        cv_img = self.get_cv2_img(file_path)

        # BGR→RGBに変換
        cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)

        # サイズ調整
        cv_img = self.scale_box(cv_img, view_height, view_width)

        # シーン作成
        height, width, dim = cv_img.shape
        bytesPerLine = dim * width
        scene = QGraphicsScene()
        image = QImage(cv_img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        item = QGraphicsPixmapItem(QPixmap.fromImage(image))
        scene.addItem(item)

        return scene

    def scale_box(self, cv_img, width, height):
        """
        アスペクト比を維持したまま画像サイズを調整る
        :param cv_img: 画像データ
        :param width: 高さ
        :param height: 幅
        :return: 調整後画像データ
        """

        h, w = cv_img.shape[:2]
        aspect = w / h
        if width / height >= aspect:
            nh = height
            nw = round(nh * aspect)
        else:
            nw = width
            nh = round(nw / aspect)

        dst = cv2.resize(cv_img, dsize=(nw, nh))

        return dst

    def get_cv2_img(self, file_path):
        """
        cv2の画像データを取得
        :param file_path: 画像ファイルパス
        :return: cv2画像データ
        """
        cv_img = cv2.imread(file_path)

        return cv_img

    def get_blank_scene(self):
        """
        空のシーン取得(初期化用)
        """
        scene = QGraphicsScene()
        return scene
