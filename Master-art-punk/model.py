#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Author ：蒋虎成
@Date   ：2021/9/24 19:12
@Desc   ：模型训练
=================================================="""
import csv
import settings
from colors import get_main_colors, colour_distance, box_method, rgb_to_hex
import numpy as np

black_rbg = [0, 0, 0]
color_data_distance = []
case_number = 8

color_distance_csv = open(settings.color_distance_filepath, "a+", newline="", encoding="utf-8-sig")
color_data = get_main_colors(settings.color_data_path)

writer = csv.writer(color_distance_csv)

for rbg in color_data:
    color_data_distance.append(rbg + [colour_distance(rbg, black_rbg)])

color_data_sort = sorted(color_data_distance, key=lambda x: x[3])
color_data_sort = np.array(color_data_sort)
color_data_sort_index = (color_data_sort[:, 3] > 300)
color_data_sort = color_data_sort[color_data_sort_index]

for rbg in color_data:
    print(rbg)
    # writer.writerow([str(colour_distance(rbg,black_rbg))])
    writer.writerow(tuple(rbg))

print(color_data_sort)
box = box_method(color_data_sort.tolist(), len(color_data_sort) // case_number)
print([rgb_to_hex(i[:3]) for i in box])
