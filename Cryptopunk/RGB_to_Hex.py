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
        # 将R、G、B分别转化为16进制拼接转换并大写  hex() 函数用于将10进制整数转换成16进制，以字符串形式表示
        color += str(hex(num))[-2:].replace('x', '0').lower()
    print(color)
    print(rgb)
    return color