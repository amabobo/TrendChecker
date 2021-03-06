# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from ui.TCMainView import Ui_frmMainView
from ui.TCGraphView import Ui_frmGraphView
from ui.TCProgressView import Ui_frmProgressView
from util.FileUtil import FileUtil
from util.ImageUtil import ImageUtil
from util.GraphProcessThread import GraphProcessThread


class TrendCheckerMainView(QMainWindow):
    """
    トレンドチェッカー メインビュー
    """

    graph_proc_th = GraphProcessThread()
    """
    グラフ処理スレッド
    """

    prog_view = None
    """
    プログレスバー表示画面
    """

    file_util = None
    """
    ファイル操作クラス
    """

    image_util = None
    """
    画像操作クラス
    """

    graph_util = None
    """
    グラフ操作クラス
    """

    normal_image_paths = list()
    """
    通常画像パス格納配列
    """

    analysis_image_paths = list()
    """
    解析画像パス格納配列
    """

    cutout_image_paths = list()
    """
    切り抜き画像パス格納配列
    """

    mini_image_objects = list()
    """
    ミニ画像オブジェクト格納配列
    """

    def __init__(self, parent=None):
        """
        コンストラクタ
        """

        # UI呼び出し
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_frmMainView()
        self.ui.setupUi(self)

        # ミニ画像オブジェクトを配列に格納
        self.mini_image_objects = [
            self.ui.viewMiniImage1,
            self.ui.viewMiniImage2,
            self.ui.viewMiniImage3,
            self.ui.viewMiniImage4,
            self.ui.viewMiniImage5,
        ]

        # オブジェクト設定
        self.ui.viewMainImage.setVisible(False)

        for mini_image_obj in self.mini_image_objects:
            mini_image_obj.setVisible(False)
            mini_image_obj.installEventFilter(self)

        self.ui.btnGraphDisplay.setEnabled(False)
        self.ui.chbMarkClothes.setEnabled(False)

        # シグナルを受信する関数を指定
        self.graph_proc_th.end_signal.connect(self.graph_proc_end)
        self.graph_proc_th.prog_signal.connect(self.graph_progress)

    def eventFilter(self, source, event):
        """
        イベント追加
        :param source:
        :param event:
        :return:
        """
        # マウスクリック時イベント
        if event.type() == QEvent.MouseButtonPress:
            if event.button() == 1:
                push_num = None

                # 押されたimageによって処理分岐
                if source.objectName() == self.ui.viewMiniImage1.objectName():
                    push_num = 0
                elif source.objectName() == self.ui.viewMiniImage2.objectName():
                    push_num = 1
                elif source.objectName() == self.ui.viewMiniImage3.objectName():
                    push_num = 2
                elif source.objectName() == self.ui.viewMiniImage4.objectName():
                    push_num = 3
                elif source.objectName() == self.ui.viewMiniImage5.objectName():
                    push_num = 4

                # ImageUtil存在チェック
                if self.image_util is None:
                    self.image_util = ImageUtil()

                # シーン取得
                if self.ui.chbMarkClothes.checkState():
                    scene = self.image_util.create_scene(self.analysis_image_paths[push_num], 400, 300)
                else:
                    scene = self.image_util.create_scene(self.normal_image_paths[push_num], 400, 300)

                # 表示領域にシーンを設定
                self.ui.viewMainImage.setScene(scene)

        return QWidget.eventFilter(self, source, event)

    def file_select_click(self):
        """
        ファイル選択ボタン押下時関数
        """

        # FileUtil存在チェック
        if self.file_util is None:
            self.file_util = FileUtil()

        # ImageUtil存在チェック
        if self.image_util is None:
            self.image_util = ImageUtil()

        # ファイルのパスを取得
        file_path = self.file_util.get_file_path()

        # ファイル選択チェック
        if file_path == "":
            return

        # 配列、オブジェクト初期化
        self.clear()

        # 画像パス配列にパスを格納
        self.normal_image_paths.append(file_path)

        # 選択したパス情報を設定
        self.ui.txtPath.setText(file_path)

        # シーン取得
        scene = self.image_util.create_scene(self.ui.txtPath.text(), 400, 300)

        # 表示領域にシーンを設定
        self.ui.viewMainImage.setScene(scene)
        self.ui.viewMainImage.setVisible(True)

        # ボタン有効化
        self.ui.btnGraphDisplay.setEnabled(True)
        self.ui.chbMarkClothes.setEnabled(True)

    def folder_select_click(self):
        """
        フォルダ選択ボタン押下時関数
        """

        # FileUtil存在チェック
        if self.file_util is None:
            self.file_util = FileUtil()

        # ImageUtil存在チェック
        if self.image_util is None:
            self.image_util = ImageUtil()

        # フォルダのパスを取得
        folder_path = self.file_util.get_folder_path()

        # フォルダ選択チェック
        if folder_path == "":
            return

        # 配列、オブジェクト初期化
        self.clear()

        # 選択したパス情報を設定
        self.ui.txtPath.setText(folder_path)

        # 選択したフォルダ内の画像パスを取得
        self.normal_image_paths = self.file_util.get_image_paths(self.ui.txtPath.text())

        # 画像パス存在チェック
        if len(self.normal_image_paths) == 0:
            return

        # 画像をセット
        self.set_mini_images(self.normal_image_paths)

        # ボタン有効化
        self.ui.btnGraphDisplay.setEnabled(True)
        self.ui.chbMarkClothes.setEnabled(True)

    def graph_display_click(self):
        """
        グラフ表示ボタン押下時関数
        """

        # グラフ処理スレッド起動
        if self.ui.chbMarkClothes.checkState():
            self.graph_proc_th.process_start(self.analysis_image_paths)
        else:
            self.graph_proc_th.process_start(self.normal_image_paths)

        # ProgressView存在チェック
        if self.prog_view is None:
            self.prog_view = TrendCheckerProgressView(self)

        # プログレスバー用画面表示
        self.prog_view.show()

    def graph_proc_end(self, file_name):
        """
        グラフ作成処理終了時に実行する
        """

        # プログレスバー画面終了
        self.prog_view.close()

        # ImageUtil存在チェック
        if self.image_util is None:
            self.image_util = ImageUtil()

        # グラフビュー表示
        graph_view = TrendCheckerGraphView(self)
        graph_view.set_graph_image(self.image_util, file_name)
        graph_view.show()

    def graph_progress(self, progress):
        """
        プログレスバー更新
        """
        self.prog_view.set_progress(progress)

    def clothes_change_toggle(self, is_checked):
        """
        服認識トグル変更時処理
        """

        # チェックした時
        if is_checked:

            # ImageUtil存在チェック
            if self.image_util is None:
                self.image_util = ImageUtil()

            # FileUtil存在チェック
            if self.file_util is None:
                self.file_util = FileUtil()

            # すでに解析画像が存在する場合はそれを使う
            if not self.analysis_image_paths:
                # 画像解析
                self.image_util.analysis_image(self.normal_image_paths)

                # 選択したフォルダ内の画像パスを取得
                self.analysis_image_paths = self.file_util.get_image_paths("./temp_work/analysis_img")

                # 解析画像存在チェック
                if len(self.analysis_image_paths) == 0:
                    self.ui.chbMarkClothes.setChecked(False)
                    return

            # 通常画像のパス以外をクリア
            self.clear_at_analysis()

            # 画像をセット
            self.set_mini_images(self.analysis_image_paths)

        # チェック外した時
        else:
            # 通常画像のパス以外をクリア
            self.clear_at_analysis()

            # 画像をセット
            self.set_mini_images(self.normal_image_paths)

    def set_mini_images(self, file_paths):
        """
        ミニ画像用オブジェクトに画像をセットする
        """
        # インデックス
        mini_image_idx = 0

        # ミニ画像オブジェクトでループ
        for mini_image_obj in self.mini_image_objects:

            if not file_paths:
                break

            if mini_image_idx >= len(file_paths):
                break

            # 初回ループチェック
            if mini_image_idx == 0:

                # 初回の場合はメイン画像、ミニ画像両方にセット
                main_scene = self.image_util.create_scene(file_paths[mini_image_idx], 400, 300)
                mini_scene = self.image_util.create_scene(file_paths[mini_image_idx], 70, 70)

                self.ui.viewMainImage.setScene(main_scene)
                self.ui.viewMainImage.setVisible(True)
                mini_image_obj.setScene(mini_scene)
                mini_image_obj.setVisible(True)

            else:
                mini_scene = self.image_util.create_scene(file_paths[mini_image_idx], 70, 70)
                mini_image_obj.setScene(mini_scene)
                mini_image_obj.setVisible(True)

            # インデックスを次に進める
            mini_image_idx += 1

    def clear(self):
        """
        クリア処理
        """

        # ImageUtil存在チェック
        if self.image_util is None:
            self.image_util = ImageUtil()

        # FileUtil存在チェック
        if self.file_util is None:
            self.file_util = FileUtil()

        # 画像パス配列を初期化
        self.normal_image_paths = list()
        self.analysis_image_paths = list()

        # オブジェクト初期化
        self.ui.chbMarkClothes.setChecked(False)

        blank_scene = self.image_util.get_blank_scene()

        self.ui.viewMainImage.setVisible(False)
        self.ui.viewMainImage.setScene(blank_scene)

        for mini_image_obj in self.mini_image_objects:
            mini_image_obj.setVisible(False)
            mini_image_obj.setScene(blank_scene)

        # 作業ディレクトリ削除
        self.file_util.delete_dir("./temp_work")

    def clear_at_analysis(self):
        """
        解析時のクリア処理
        """

        # ImageUtil存在チェック
        if self.image_util is None:
            self.image_util = ImageUtil()

        # オブジェクト初期化
        blank_scene = self.image_util.get_blank_scene()

        self.ui.viewMainImage.setVisible(False)
        self.ui.viewMainImage.setScene(blank_scene)

        for mini_image_obj in self.mini_image_objects:
            mini_image_obj.setVisible(False)
            mini_image_obj.setScene(blank_scene)

    def closeEvent(self, event):
        """
        画面クローズ時処理
        """
        # 初期化して閉じる
        self.clear()

class TrendCheckerGraphView(QtWidgets.QDialog):
    """
    トレンドチェッカー グラフビュー
    """

    def __init__(self, parent=None):
        """
        コンストラクタ
        """

        # UI呼び出し
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = Ui_frmGraphView()
        self.ui.setupUi(self)

    def show(self):
        """
        グラフビューを表示する
        """

        self.exec_()

    def back_click(self):
        """
        戻るボタン押下時関数
        """

        # グラフビューを閉じる
        self.close()

    def set_graph_image(self, image_util, graph_image_path):
        """
        グラフ画像を設定
        """

        # シーン取得
        scene = image_util.create_scene(graph_image_path, 400, 300)

        # グラフ画像を描画
        self.ui.viewGraphImage.setScene(scene)


class TrendCheckerProgressView(QtWidgets.QDialog):
    """
    トレンドチェッカー プログレスビュー
    """

    main_view = None

    def __init__(self, parent=None):
        """
        コンストラクタ
        """

        # UI呼び出し
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = Ui_frmProgressView()
        self.ui.setupUi(self)

        # ラベルにロード時のgifをセット
        self.movie = QMovie("img/loading2.gif")
        self.ui.lblLoad.setMovie(self.movie)
        self.movie.start()

        # メイン画面取得
        self.main_view = parent

    def show(self):
        """
        グラフビューを表示する
        """

        self.exec_()

    def set_progress(self, progress):
        """
        プログレスバー値セット処理
        """
        self.ui.pgbGraph.setValue(progress)

    def closeEvent(self, event):
        """
        画面クローズ時処理
        """
        # スレッドを止める
        main_view.graph_proc_th.process_stop()


if __name__ == '__main__':
    app_main_view = QtWidgets.QApplication(sys.argv)
    main_view = TrendCheckerMainView()
    main_view.show()
    sys.exit(app_main_view.exec_())
