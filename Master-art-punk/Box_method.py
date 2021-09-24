#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Cryptopunk -> Box_method
@IDE    ：PyCharm
@Author ：蒋虎成
@Date   ：2021/9/24 20:54
@Desc   ：
=================================================='''
import random
def box_method(colordata,group_distance):
    colordata_random_box = []
    for i in range(0,8):
        colordata_random_box.append(colordata[(len(colordata) - 1) - (i * group_distance + random.randint(0,group_distance-1))])
    return colordata_random_box