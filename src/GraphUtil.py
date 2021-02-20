# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib as mpl
from EnumColors import EnumColors
from matplotlib.font_manager import FontProperties
from datetime import datetime

"""
グラフを画像ファイルに出力します。
"""
def createGraph(colors):
    
    # 合計
    sumAll = 0
    for valColor in colors:
        sumAll += int(colors[valColor])
    
    # その他
    valSonota = 0
    for valColor in colors:
        if (int(colors[valColor]) / sumAll < 0.025) :
            valSonota += int(colors[valColor])
            colors[valColor] = 0
        
    # 並べ替え
    sortColors = sorted(colors.items(), key=lambda x:x[1], reverse=True)
    
    # ラベル、色、値を設定
    gLabels = list()
    gColors = list()
    gValues = list()
    for key, value in sortColors :
        if (int(colors[key]) > 0) :
            enum = EnumColors.value_of(key)
            gLabels.append(enum.nm)
            gColors.append(enum.code)
            gValues.append(value)
            
    # その他を設定         
    #gLabels.append("その他")
    #gColors.append("0.9")
    #gValues.append(valSonota)

    # フォントを指定します。
    fp = FontProperties(fname='C:\WINDOWS\Fonts\meiryo.ttf', size=8)
    
    # グラフの描画先の準備
    fig = plt.figure()
    
    # 描画設定
    fig, ax = plt.subplots()
    patches, texts, autotexts = ax.pie(gValues, colors=gColors, autopct='%1.1f%%', pctdistance=1.12, wedgeprops={'linewidth': 1, 'edgecolor':"black"}, radius=1.4, startangle=90, counterclock=False)
    
    # フォントを設定します。
    plt.setp(texts, FontProperties=fp)
    
    # 凡例を設定
    #plt.legend(gLabels, fancybox=True, loc='upper left', bbox_to_anchor=(1.05, 1.05), borderaxespad=0)

    # グラフを表示します。
    plt.show()

    # 日時を取得
    dt = datetime.now()

    # ファイル名を設定
    fileName = "img_" + dt.strftime('%Y') + dt.strftime('%m') + dt.strftime('%d') + dt.strftime('%H') + dt.strftime('%M') + dt.strftime('%S') + ".png"

    # 画像を保存します。
    fig.savefig("img/" + fileName)

    return fileName

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