# -*- coding: utf-8 -*-

from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
from datetime import datetime

from .EnumColors import EnumColors
from .ImageUtil import ImageUtil
from .FileUtil import FileUtil


class GraphUtil:
    """
    グラフ操作クラス
    """
    # BGR配列のインデックス
    BGR_RED_IDX = 2
    BGR_GREEN_IDX = 1
    BGR_BLUE_IDX = 0

    # RGB配列のインデックス
    RGB_RED_IDX = 0
    RGB_GREEN_IDX = 1
    RGB_BLUE_IDX = 2

    progress = 0
    """
    進捗
    """

    def get_color_ratio(self, file_paths, proc_thread):
        """
        画像ファイルから色の割合を取得
        :param file_paths: ファイル群
        :param proc_thread: 処理中のスレッド
        :return: 色割合Dictionary
        """

        self.progress = 0

        # 全色のDictionaryを作成
        color_dic = {EnumColors.COLOR_WHITE.name: 0,
                     EnumColors.COLOR_OLIVE.name: 0,
                     EnumColors.COLOR_YELLOW.name: 0,
                     EnumColors.COLOR_FUCHSIA.name: 0,
                     EnumColors.COLOR_AQUA.name: 0,
                     EnumColors.COLOR_RED.name: 0,
                     EnumColors.COLOR_GRAY.name: 0,
                     EnumColors.COLOR_BLUE.name: 0,
                     EnumColors.COLOR_GREEN.name: 0,
                     EnumColors.COLOR_PURPLE.name: 0,
                     EnumColors.COLOR_BLACK.name: 0,
                     EnumColors.COLOR_MAROON.name: 0}

        # ImageUtilを取得
        img_util = ImageUtil()

        # 進捗更新 5
        #self.progress += 5
        #proc_thread.prog_signal.emit(self.progress)

        # 全ファイルを処理
        for file_path in file_paths:

            print("loadStart:" + file_path)

            # 画像を読み込み、RGBを取得
            bgr_array = img_util.get_cv2_img(file_path)

            # RGBをチェック
            for i in range(bgr_array.shape[0]):
                for j in range(bgr_array.shape[1]):

                    # 取得した色
                    rgb = bgr_array[i, j]

                    # 色結果
                    result_color = None

                    # 基準値にどれぐらい近いか　0に近いほど近い
                    near = None

                    # 基準値の判定
                    for color in EnumColors:

                        # 基準値を取得
                        kjnRgb = color.rgb

                        # 基準値との差を算出
                        r = abs(rgb[self.BGR_RED_IDX] - kjnRgb[self.RGB_RED_IDX])
                        g = abs(rgb[self.BGR_GREEN_IDX] - kjnRgb[self.RGB_GREEN_IDX])
                        b = abs(rgb[self.BGR_BLUE_IDX] - kjnRgb[self.RGB_BLUE_IDX])
                        diff = r + g + b

                        # 暫定の基準値に更新
                        if near is None or near > diff:
                            result_color = color.name
                            near = diff

                    color_dic[result_color] += 1
                    
                # 進捗更新
                num = 100 / len(range(bgr_array.shape[0])) / len(file_paths) 
                self.progress += num
                proc_thread.prog_signal.emit(self.progress)

            print("loadEnd  :" + file_path)

            # 進捗更新 85
            #self.progress += 80 / len(file_paths)
            #proc_thread.prog_signal.emit(self.progress)

        print("↓count↓")

        # 色の割合を出力
        for color in color_dic:
            print(str(color) + ":" + str(color_dic[color]))

        return color_dic

    def create_graph(self, color_dic, proc_thread):
        """
        グラフを画像ファイルに出力
        :param color_dic: 色配列
        :param proc_thread: 処理中のスレッド
        :return: ファイルパス
        """

        # 合計
        sum_all = 0
        for val_color in color_dic:
            sum_all += int(color_dic[val_color])

        # その他
        val_other = 0
        for val_color in color_dic:
            if int(color_dic[val_color]) / sum_all < 0.025:
                val_other += int(color_dic[val_color])
                color_dic[val_color] = 0

        # 進捗更新 90
        #self.progress += 5
        #proc_thread.prog_signal.emit(self.progress)

        # 並べ替え
        sort_colors = sorted(color_dic.items(), key=lambda x: x[1], reverse=True)

        # ラベル、色、値を設定
        gLabels = list()
        gColors = list()
        gValues = list()
        for key, value in sort_colors:
            if int(color_dic[key]) > 0:
                enum = EnumColors.value_of(key)
                gLabels.append(enum.nm)
                gColors.append(enum.code)
                gValues.append(value)

        # 進捗更新 95
        #self.progress += 5
        proc_thread.prog_signal.emit(self.progress)

        # その他を設定
        # gLabels.append("その他")
        # gColors.append("0.9")
        # gValues.append(valSonota)

        # フォントを指定
        fp = FontProperties(fname='C:\WINDOWS\Fonts\meiryo.ttf', size=8)

        # グラフの描画先の準備
        fig = plt.figure()

        # 描画設定
        fig, ax = plt.subplots()
        patches, texts, autotexts = ax.pie(gValues, colors=gColors, autopct='%1.1f%%', pctdistance=1.12,
                                           wedgeprops={'linewidth': 1, 'edgecolor': "black"}, radius=1.4, startangle=90,
                                           counterclock=False)

        # フォントを設定
        plt.setp(texts, FontProperties=fp)

        # 凡例を設定
        # plt.legend(gLabels, fancybox=True, loc='upper left', bbox_to_anchor=(1.05, 1.05), borderaxespad=0)

        # グラフを表示
        # plt.show()

        # FileUtil取得
        file_util = FileUtil()

        result_path = "./img/result"

        # ディレクトリ作成
        file_util.create_dir(result_path)

        # 日時を取得
        dt = datetime.now()

        # ファイル名を設定
        file_name = "graph_img_{}{}{}{}{}{}.png".format( dt.strftime('%Y'), dt.strftime('%m'), dt.strftime('%d'),
                                                         dt.strftime('%H'), dt.strftime('%M'), dt.strftime('%S'))

        file_full_path = "{}/{}".format(result_path, file_name)

        # 画像を保存
        fig.savefig(file_full_path)

        # 進捗更新 100
        #self.progress += 5
        #proc_thread.prog_signal.emit(self.progress)

        return file_full_path
