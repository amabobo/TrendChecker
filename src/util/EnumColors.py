# -*- coding: utf-8 -*-

from enum import Enum


class EnumColors(Enum):
    """
    色定義Enum

    色定義参考：　https://note.cman.jp/color/base_color.cgi
    """

    #　　 Enum名   = (ID,      RGB,       カラーコード, 名前)
    COLOR_WHITE   = (0 , [255, 255, 255], "#ffffff", "白")
    COLOR_OLIVE   = (1 , [128, 128,   0], "#808000", "オリーブ")
    COLOR_YELLOW  = (2 , [255, 255,   0], "#ffff00", "黄")
    COLOR_FUCHSIA = (3 , [255,   0, 255], "#ff00ff", "ピンク")
    COLOR_AQUA    = (4 , [  0, 255, 255], "#00ffff", "水色")
    COLOR_RED     = (5 , [255,   0,   0], "#ff0000", "赤")
    COLOR_GRAY    = (6 , [128, 128, 128], "#808080", "グレー")
    COLOR_BLUE    = (7 , [  0,   0, 255], "#0000ff", "青")
    COLOR_GREEN   = (8 , [  0, 128,   0], "#008000", "緑")
    COLOR_PURPLE  = (9 , [128,   0, 128], "#800080", "紫")
    COLOR_BLACK   = (10, [  0,   0,   0], "#000000", "黒")
    COLOR_MAROON  = (11, [128,   0,   0], "#800000", "茶")

    @classmethod
    def value_of(cls, targetName):
        """
        文字列から該当のEnumColorsを取得
        :param targetName: 取得したいEnumColorsのname
        :return: 該当のEnumColors
        """
        for e in EnumColors:
            if e.name == targetName:
                return e
        raise ValueError('{} は有効なEnumではありません'.format(targetName))

    def __init__(self, id, rgb, code, nm):
        """
        コンストラクタ
        :param id: 一意ID
        :param rgb: RGB
        :param code: カラーコード
        :param nm: 名前
        """
        self.id = id
        self.rgb = rgb
        self.code = code
        self.nm = nm