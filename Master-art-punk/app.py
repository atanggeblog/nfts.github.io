#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Author ：蒋虎成
@Date   ：2021/9/22 17:04
@Desc   ：主接口
=================================================="""
from colors import ColorMultiImage
import settings
from model import training
if __name__ == '__main__':
    generate_color = ColorMultiImage()
    stickers = settings.module  # 设置模组已经内置mouse和cattle
    if settings.train:
        color_model_path = training(settings.color_data_path)
        print("颜色模型生成路径:" + color_model_path)
    for amount in range(0, settings.n):  # 设置生成数量
        pixel = generate_color.merges(stickers)
        colors_number = generate_color.colors_number
        generate_color.generate(pixel, settings.color_output_name,str(amount),settings.color_model_path,settings.color_style,colors_number)
        print(f"INFO:生成第{str(amount)}个{settings.color_output_name}")