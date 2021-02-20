# -*- coding: utf-8 -*-

import cv2
from EnumColors import EnumColors

# BGR配列のインデックス
BGR_RED_IDX = 2
BGR_GREEN_IDX = 1
BGR_BLUE_IDX = 0

# RGB配列のインデックス
RGB_RED_IDX = 0
RGB_GREEN_IDX = 1
RGB_BLUE_IDX = 2

def start(files):    
    """
    画像ファイルから色の割合を取得
    :param files: ファイル群
    """

    # 全色のDictonaryを作成
    dicColor = {EnumColors.COLOR_WHITE.name   :0,
                EnumColors.COLOR_OLIVE.name   :0,
                EnumColors.COLOR_YELLOW.name  :0,
                EnumColors.COLOR_FUCHSIA.name :0,
                EnumColors.COLOR_AQUA.name    :0,
                EnumColors.COLOR_RED.name     :0,
                EnumColors.COLOR_GRAY.name    :0,
                EnumColors.COLOR_BLUE.name    :0,
                EnumColors.COLOR_GREEN.name   :0,
                EnumColors.COLOR_PURPLE.name  :0,
                EnumColors.COLOR_BLACK.name   :0,
                EnumColors.COLOR_MAROON.name  :0}

    # 全ファイルを処理
    for filePath in files:
    
        print("loadStart:" + filePath)

        # 画像を読み込み、RGBを取得
        bgrArray = cv2.imread(filePath)
    
        # RGBをチェック
        for i in range(bgrArray.shape[0]):
            for j in range(bgrArray.shape[1]):
               
                # 取得した色
                rgb = bgrArray[i, j]
                
                # 色結果
                resultColor = None
                
                # 基準値にどれぐらい近いか　0に近いほど近い 
                near = None;
    
                # 基準値の判定
                for color in EnumColors:
                    
                    # 基準値を取得
                    kjnRgb = color.rgb
                    
                    # 基準値との差を算出
                    r = abs(rgb[BGR_RED_IDX] - kjnRgb[RGB_RED_IDX])
                    g = abs(rgb[BGR_GREEN_IDX] - kjnRgb[RGB_GREEN_IDX])
                    b = abs(rgb[BGR_BLUE_IDX] - kjnRgb[RGB_BLUE_IDX])
                    diff = r + g + b
                    
                    # 暫定の基準値に更新
                    if (near == None or near > diff):
                        resultColor = color.name
                        near = diff
    
                dicColor[resultColor] += 1
    
        print("loadEnd  :" + filePath)

    # カウント数をパーセントに置き換えます。
    #for color in dicColor:
    #    dicColor[color] = dicColor[color]

    print("↓count↓")
    
    # 色の割合を出力
    for color in dicColor: 
        print(str(color) + ":" + str(dicColor[color]))
    
    return dicColor
    