import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from .FileUtil import FileUtil


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

    def analysis_image(self, file_paths):
        """
        画像解析を行い、結果を反映した画像を返す
        """

        # カスケード分類器(学習データ)のパス
        cascade_path = "./model/haarcascade_fullbody.xml"

        # 解析後画像格納フォルダパス
        analysis_image_dir_path = "./temp_work/analysis_img"

        # 切り出し画像格納フォルダパス
        cutout_image_dir_path = "./temp_work/cutout_img"

        # 解析画像格納先フォルダ生成
        FileUtil.create_dir(analysis_image_dir_path)

        # 切り出し画像格納先フォルダ生成
        FileUtil.create_dir(cutout_image_dir_path)

        # ファイルパスインデックス
        fileIdx = 0

        for file_path in file_paths:

            fileIdx += 1

            # ファイル読み込み
            image = cv2.imread(file_path)

            # グレースケール変換
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # カスケード分類器の特徴量を取得する
            cascade = cv2.CascadeClassifier(cascade_path)

            # 物体認識の実行
            # image – CV_8U 型の行列．ここに格納されている画像中から物体が検出されます
            # objects – 矩形を要素とするベクトル．それぞれの矩形は，検出した物体を含みます
            # scaleFactor – 各画像スケールにおける縮小量を表します
            # minNeighbors – 物体候補となる矩形は，最低でもこの数だけの近傍矩形を含む必要があります
            # flags – このパラメータは，新しいカスケードでは利用されません．古いカスケードに対しては，cvHaarDetectObjects 関数の場合と同じ意味を持ちます
            # minSize – 物体が取り得る最小サイズ．これよりも小さい物体は無視されます
            analysis_rect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))

            color = (255, 0, 0)  # 青

            # 検出した場合
            if len(analysis_rect) > 0:

                # 検出した部分を囲む矩形の作成
                for rect in analysis_rect:
                    cv2.rectangle(image, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), color, thickness=2)

                # 切り出し画像インデックス
                cutoutIdx = 0

                # 切り出し処理
                for x, y, w, h in analysis_rect:

                    cutoutIdx += 1

                    # 切り出し実行
                    cutout_img = image[y:y + h, x:x + w]

                    # 切り出し画像名
                    cutout_image_name = "cutout_{}_{}.jpg".format(fileIdx, cutoutIdx)

                    # 切り出し画像パス
                    cutout_image_full_path = "{}/{}".format(cutout_image_dir_path, cutout_image_name)

                    # 切り抜き画像の保存
                    cv2.imwrite(cutout_image_full_path, cutout_img)

                # 解析画像名
                analysis_image_name = "analysis_{}.jpg".format(fileIdx)

                # 解析結果画像パス
                analysis_image_full_path = "{}/{}".format(analysis_image_dir_path, analysis_image_name)

                # 解析結果画像の保存
                cv2.imwrite(analysis_image_full_path, image)


