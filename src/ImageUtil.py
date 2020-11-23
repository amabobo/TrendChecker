# -*- coding: utf-8 -*-

import cv2
from EnumColors import EnumColors

# RGB配列のインデックス
RED_IDX = 0
GREEN_IDX = 1
BLUE_IDX = 2 

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
    rgbArray = cv2.imread(filePath)
    
    # RGBをチェックします。
    for i in range(rgbArray.shape[0]):
        for j in range(rgbArray.shape[1]):
           
            # 取得した色
            rgb = rgbArray[i, j]
            
            # 色結果
            resultColor = None
            
            # 基準値にどれぐらい近いか　0に近いほど近い 
            near = None;

            # 基準値の判定を行います。
            for color in EnumColors:
                
                # 基準値を取得します。
                kjnRgb = color.rgb
                
                # 基準値との差を求めます。
                r = abs(rgb[RED_IDX] - kjnRgb[RED_IDX])
                g = abs(rgb[GREEN_IDX] - kjnRgb[GREEN_IDX])
                b = abs(rgb[BLUE_IDX] - kjnRgb[BLUE_IDX])
                diff = r + g + b
                
                # 暫定の基準値に更新します。
                if (near == None or near > diff):
                    resultColor = color.name
                    near = diff
                

            dicColor[resultColor] += 1

    print(rgbArray.shape)

    # カウント数をパーセントに置き換えます。
    for color in dicColor:
        dicColor[color] = dicColor[color] / (rgbArray.shape[0] * rgbArray.shape[1]) * 100


    print("カウントします。")
    
    # 色の割合を出力します。
    for color in dicColor: 
        print(color)
        print(dicColor[color])
    
    return dicColor
            
"if __name__ == '__main__':"
"""start("D:\\Users\\amabobo\\Downloads\\images.jpg")"""
    