import os
import tkinter
import glob
from tkinter import filedialog


class FileUtil:
    """
    ファイル操作クラス
    """

    @staticmethod
    def get_file_path():
        """
        ファイルを選択しファイルパスを取得する
        :return: ファイルパス
        """
        # ファイル選択時に表示される謎のウィンドウを非表示にする
        root = tkinter.Tk()
        root.withdraw()

        # ファイル種類のフィルタ指定
        fTyp = [("画像ファイル", "*.jpeg"), ("画像ファイル", "*.jpg"), ("画像ファイル", "*.png")]
        iDir = os.path.abspath(os.path.dirname(__file__))

        # 選択したファイルのパスを取得
        file_path = filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)

        return file_path

    @staticmethod
    def get_folder_path():
        """
        フォルダを選択しフォルダパスを取得する
        :return: フォルダパス
        """
        # ファイル選択時に表示される謎のウィンドウを非表示にする
        root = tkinter.Tk()
        root.withdraw()

        iDir = os.path.abspath(os.path.dirname(__file__))

        # 選択したフォルダのパスを取得
        folder_path = filedialog.askdirectory(initialdir=iDir)

        return folder_path

    @staticmethod
    def get_image_paths(folder_path):
        """
        フォルダ内の画像パスを取得
        :return: 画像パス配列
        """

        image_paths = glob.glob(folder_path + '/*.jpg')
        image_paths.extend(glob.glob(folder_path + '/*.jpeg'))
        image_paths.extend(glob.glob(folder_path + '/*.png'))

        return image_paths

    @staticmethod
    def create_dir(path):

        # ディレクトリ存在チェック
        if not os.path.isdir(path):

            # 存在しない場合作成
            os.makedirs(path)





