#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Cryptopunk -> Get_all_colors_list
@IDE    ：PyCharm
@Author ：蒋虎成
@Date   ：2021/9/24 19:39
@Desc   ：
=================================================='''
import numpy as np
def Get_all_colors_list(model,k):
    colors = []
    labels_list = np.arange(0, k + 1)
    (proportion, _) = np.histogram(model.labels_, bins=labels_list)
    proportion = proportion.astype("float")
    proportion /= proportion.sum()
    for (_, color) in sorted(zip(proportion, model.cluster_centers_), key=lambda x: x[0], reverse=True):
        colors.append(list(map(int,color)))
        #print(colors)
    return colors