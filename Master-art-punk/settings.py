#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Author ：蒋虎成
@Date   ：2021/9/24 19:12
@Desc   ： 基础配置文件
========================================d=========="""
import function.subject as subject
import function.stickers as stickers
color_data_path = './data/Monet/'  # 这里填入你的训练集文件夹路径例如：\\你的电脑路径\\data\\monet\
DATACENTER_ID = 0
WORKER_ID = 0
SEQUENCE = 0
color_model_path = "./output/csv/1442865660962013184.csv"
module = [subject.canvas, subject.cattle]
n = 10  #生成数量
color_output_name = 'cattle' #文件夹名字
color_style = 1 #0为随机风格，1为艺术家风格
k = 30  # K-Means算法分成K类
init_method = 'random'
random_state = 88
train = False
 # 艺术家风格分箱颜色数