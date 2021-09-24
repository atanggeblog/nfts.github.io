#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Cryptopunk -> Get_color_data
@IDE    ：PyCharm
@Author ：蒋虎成
@Date   ：2021/9/24 22:06
@Desc   ：
=================================================='''
import csv
from Box_method import box_method
from RGB_to_Hex import rgb_to_hex
import numpy as np
def get_color_data():
    f = open("colordistance.csv", "r+", encoding="utf-8-sig")
    reader = csv.reader(f)
    colordata_sort = list(reader)
    case_number = 8
    box = box_method(colordata_sort, len(colordata_sort) // case_number)
    return [rgb_to_hex(i[:3]) for i in box]
print(get_color_data())