# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib as mpl
from EnumColors import EnumColors
from matplotlib.font_manager import FontProperties

"""
グラフを画像ファイルに出力します。
"""
def createGraph(colors):
    
    # ラベルと色を設定します。
    gLabels = list()
    gColors = list()
    for color in EnumColors:
        gLabels.append(color.nm)
        gColors.append(color.code)
        
    # 値を設定します。
    gValues = list()
    for valColor in colors:
        gValues.append(colors[valColor])

    # フォントを指定します。
    fp = FontProperties(fname=r'C:\WINDOWS\Fonts\meiryob.ttc', size=10)
    
    # グラフの描画先の準備
    fig = plt.figure()
    
    # 描画
    fig, ax = plt.subplots()
    patches, texts, autotexts = ax.pie(gValues, colors=gColors, labels=gLabels, autopct="%1.1f %%")
    
    # フォントを設定します。
    plt.setp(texts, FontProperties=fp)
        
    # グラフを表示します。
    plt.show()

    # 画像を保存します。
    fig.savefig("img.png")

    return "img.png"

if __name__ == '__main__':
    
    dicColor = {EnumColors.COLOR_WHITE   :100,
                EnumColors.COLOR_OLIVE   :10,
                EnumColors.COLOR_YELLOW  :10,
                EnumColors.COLOR_FUCHSIA :30,
                EnumColors.COLOR_AQUA    :10,
                EnumColors.COLOR_RED     :10,
                EnumColors.COLOR_GRAY    :60,
                EnumColors.COLOR_BLUE    :10,
                EnumColors.COLOR_GREEN   :10,
                EnumColors.COLOR_PURPLE  :10,
                EnumColors.COLOR_BLACK   :10,
                EnumColors.COLOR_MAROON  :10}
    
    createGraph(dicColor)