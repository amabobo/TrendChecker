# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib as mpl
from EnumColors import EnumColors
from matplotlib.font_manager import FontProperties

"""
グラフを画像ファイルに出力します。
"""
def createGraph(colors):
    
    # convert
    sumAll = 0
    for valColor in colors:
        sumAll += int(colors[valColor])
    
    valSonota = 0
    for valColor in colors:
        if (int(colors[valColor]) / sumAll < 0.01) :
            valSonota += int(colors[valColor])
            colors[valColor] = 0
        
    
    # ラベルと色を設定します。
    gLabels = list()
    gColors = list()
    for color in EnumColors:
        if (int(colors[color.name]) > 0) :
            gLabels.append(color.nm)
            gColors.append(color.code)
        
    #gLabels.append("sonota")
    #gColors.append("#00000000")
        
    # 値を設定します。
    gValues = list()
    for valColor in colors:
        if (int(colors[valColor]) > 0) :
            gValues.append(colors[valColor])
        
    #gValues.append(valSonota)

    # フォントを指定します。
    fp = FontProperties(fname=r'C:\WINDOWS\Fonts\meiryob.ttc', size=10)
    
    # グラフの描画先の準備
    fig = plt.figure()
    
    # 描画
    fig, ax = plt.subplots()
    patches, texts, autotexts = ax.pie(gValues, colors=gColors, autopct='%1.1f%%', pctdistance=1.1, shadow=True, radius=1.6)
    
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