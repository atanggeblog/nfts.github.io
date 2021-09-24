#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Cryptopunk -> Generate-crypto-punk
@IDE    ：PyCharm
@Author ：蒋虎成
@Date   ：2021/9/22 17:02
@Desc   ：
=================================================='''
import png
from Image_subject import canvas, man, woman, mouse, cattle
from Image_stickers import cigarette, hairman, hairwoman
import random
from Get_color_data import get_color_data
def randomcolor():
    colorArr = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    color = ""
    for i in range(6):
        color += colorArr[random.randint(0,14)]
    return color
def merge(sticker0, sticker1):
    colors = sticker0['colors']
    index = {}
    for i,color in enumerate(sticker1['colors']):
        if color not in colors:
            colors.append(color)
            index[i] = colors.index(color)
            print(colors.index(color))
        else:
            index[i] = colors.index(color)

    for i,row in enumerate(sticker1['data']):
        for j,color in enumerate(row):
            if color > 0:
                sticker0['data'][i][j] = index[color]
    return sticker0


def merges(stickers):
    if len(stickers) >= 2:
        sticker = merge(stickers.pop(0), stickers.pop(0))
        stickers.insert(0, sticker)
    else:
        return stickers[0]
    return merges(stickers)


def generate(image, name):
    #colors = image['colors'][1:]
    palette = [(255, 255, 255,0)]
    #colors = ['000000'] + [randomcolor() for i in range(0,8)]
    colors = ['000000'] + get_color_data()
    print(colors)
    for color in colors:
        color = [int(c, 16) for c in (color[:2], color[2:4], color[4:])]
        palette.append(tuple(color))
        print(palette)
    w = png.Writer(len(canvas['data'][0]), len(
        canvas['data']), palette=palette, bitdepth=4)
    f = open(f'output/{name}.png', 'wb')
    w.write(f, image['data'])


if __name__ == '__main__':
    stickers = [canvas,mouse] #设置模组已经内置mouse和cattle
    for i in range(0,100):  #设置生成数量
        image = merges(stickers)
        generate(image, 'monet-output/monet-cattle' + str(i))