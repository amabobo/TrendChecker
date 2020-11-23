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

def start(filePath):    

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
            
    # 画像を読み込み、RGBを取得します。
    bgrArray = cv2.imread(filePath)
    
    # RGBをチェックします。
    for i in range(bgrArray.shape[0]):
        for j in range(bgrArray.shape[1]):
           
            # 取得した色
            rgb = bgrArray[i, j]
            
            # 色結果
            resultColor = None
            
            # 基準値にどれぐらい近いか　0に近いほど近い 
            near = None;

            # 基準値の判定を行います。
            for color in EnumColors:
                
                # 基準値を取得します。
                kjnRgb = color.rgb
                
                # 基準値との差を求めます。
                r = abs(rgb[BGR_RED_IDX] - kjnRgb[RGB_RED_IDX])
                g = abs(rgb[BGR_GREEN_IDX] - kjnRgb[RGB_GREEN_IDX])
                b = abs(rgb[BGR_RED_IDX] - kjnRgb[RGB_BLUE_IDX])
                diff = r + g + b
                
                # 暫定の基準値に更新します。
                if (near == None or near > diff):
                    resultColor = color.name
                    near = diff
                

            dicColor[resultColor] += 1

    print(bgrArray.shape)

    # カウント数をパーセントに置き換えます。
    for color in dicColor:
        dicColor[color] = dicColor[color] / (bgrArray.shape[0] * bgrArray.shape[1]) * 100


    print("カウントします。")
    
    # 色の割合を出力します。
    for color in dicColor: 
        print(color)
        print(dicColor[color])
    
    return dicColor
            
"if __name__ == '__main__':"
"""start("D:\\Users\\amabobo\\Downloads\\images.jpg")"""
    