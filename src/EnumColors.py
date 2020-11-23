# -*- coding: utf-8 -*-

from enum import Enum

# 色
"https://note.cman.jp/color/base_color.cgi"
class EnumColors(Enum):
    COLOR_WHITE   = (0 , [255, 255, 255], "#ffffff", "白")
    COLOR_OLIVE   = (1 , [128, 128,   0], "#808000", "オリーブ")
    COLOR_YELLOW  = (2 , [255, 255,   0], "#ffff00", "黄")
    COLOR_FUCHSIA = (3 , [255,   0, 255], "#ff00ff", "ピンク")
    COLOR_AQUA    = (5 , [  0, 255, 255], "#00ffff", "水色")
    COLOR_RED     = (7 , [255,   0,   0], "#ff0000", "赤")
    COLOR_GRAY    = (8 , [128, 128, 128], "#808080", "グレー")
    COLOR_BLUE    = (9 , [  0,   0, 255], "#0000ff", "青")
    COLOR_GREEN   = (10, [  0, 128,   0], "#008000", "緑")
    COLOR_PURPLE  = (11, [128,   0, 128], "#800080", "紫")
    COLOR_BLACK   = (12, [  0,   0,   0], "#000000", "黒")
    COLOR_MAROON  = (15, [128,   0,   0], "#800000", "茶")
    
    def __init__(self, id, rgb, code, nm):
        self.id = id
        self.rgb = rgb
        self.code = code
        self.nm = nm
    
if __name__ == "__main__":
    print('#=== ja ===#')
    print(EnumColors.COLOR_RED.id)
