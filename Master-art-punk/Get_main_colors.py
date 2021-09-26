#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Cryptopunk -> Get_main_colors
@IDE    ：PyCharm
@Author ：蒋虎成
@Date   ：2021/9/24 19:20
@Desc   ：
=================================================='''
import PIL
import cv2
from matplotlib import image
from KMeans_parameter import k,init,random_state
from sklearn.cluster import KMeans
from os import listdir
from Get_colors_list import Get_all_colors_list
def get_main_colors(directory):
    colors_all_out = []
    for filename in listdir(directory):
        img = cv2.imread(directory + filename)
        image2 = PIL.Image.fromarray(image.imread(directory + filename))
        img_data = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        r, g, b = cv2.split(img_data)
        # 行*列和颜色通道数（因RGB而为3个）
        img = img.reshape((img_data.shape[0]*img_data.shape[1], 3))
        print("加载"+filename+"中......")
        model = KMeans(n_clusters=k, init=init, random_state=random_state)
        model.fit(img)
        colors_all_out += Get_all_colors_list(model, k)
        print("完成"+filename+"提取!")
    return colors_all_out