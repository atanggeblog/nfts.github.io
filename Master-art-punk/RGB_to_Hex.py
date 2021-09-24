#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Cryptopunk -> RGB_to_Hex
@IDE    ：PyCharm
@Author ：蒋虎成
@Date   ：2021/9/24 21:41
@Desc   ：
=================================================='''
def rgb_to_hex(rgb):
    color = ''
    for i in rgb:
        num = round(float(i))
        color += str(hex(num))[-2:].replace('x', '0').lower()
    print(color)
    print(rgb)
    return color