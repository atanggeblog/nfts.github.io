#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Author ：蒋虎成
@Date   ：2021/9/24 19:12
@Desc   ： 基础配置文件
=================================================="""
color_data_path = './Master-art-punk/Master-art-punk/Master-art-punk/data/Monet'  # 这里填入你的训练集文件夹路径例如：\\你的电脑路径\\data\\monet\
color_distance_filepath = 'data/color_distance.csv'
k = 30  # K-Means算法分成K类
init_method = 'random'
random_state = 88
box_number = 8 # 艺术家风格分箱颜色数