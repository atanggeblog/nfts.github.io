#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Cryptopunk -> Get_color_model
@IDE    ：PyCharm
@Author ：蒋虎成
@Date   ：2021/9/24 19:12
@Desc   ：
=================================================='''
import csv
from Get_main_colors import get_main_colors
from ColourDistance import colourdistance
import numpy as np
from Box_method import box_method
from RGB_to_Hex import rgb_to_hex
f = open("colordistance.csv","a+",newline="",encoding="utf-8-sig")
colordata = get_main_colors('这里填入你的训练集文件夹路径例如：C:\\你的电脑路径\\data\\monet\\')
writer = csv.writer(f)
black_rbg = [0,0,0]
colordata_disrance = []
for rbg in colordata:
    colordata_disrance.append(rbg + [colourdistance(rbg,black_rbg)])
colordata_sort = sorted(colordata_disrance,key=lambda x:x[3])
colordata_sort = np.array(colordata_sort)
colordata_sort_index = (colordata_sort[:,3] > 300)
colordata_sort = colordata_sort[colordata_sort_index]
for rbg in colordata:
    print(rbg)
    #writer.writerow([str(colourdistance(rbg,black_rbg))])
    writer.writerow(tuple(rbg))
case_number = 8
print(colordata_sort)
box = box_method(colordata_sort.tolist(),len(colordata_sort) // case_number)
print([rgb_to_hex(i[:3]) for i in box])
