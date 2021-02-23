from PyQt5.QtCore import QThread, pyqtSignal

from .GraphUtil import GraphUtil


class GraphProcessThread(QThread):
    """
    GUIの裏でグラフ生成する場合に使用するスレッドクラス
    """

    image_paths = list()

    graph_util = GraphUtil()
    """
    GraphUtil
    """

    end_signal = pyqtSignal(str)
    """
    終了時シグナル
    """

    prog_signal = pyqtSignal(int)
    """
    プログレスシグナル
    """

    def run(self):
        """
        スレッドメイン処理
        """

        # 色割合を格納したディクショナリを取得
        image_color_dic = self.graph_util.get_color_ratio(self.image_paths, self)

        # ディクショナリを基にグラフを作成
        file_name = self.graph_util.create_graph(image_color_dic, self)

        self.end_signal.emit(file_name)

        self.quit()

    def process_start(self, image_paths):
        """
        スレッド開始処理
        :param image_paths: 画像パス
        """

        self.image_paths = image_paths

        self.start()

    def process_stop(self):
        """
        スレッド停止処理
        """

        self.terminate()

    def send_prog_signal(self,progress):
        """
        シグナル送信処理
        """
        self.prog_signal.emit(progress)
