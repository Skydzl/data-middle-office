#    Copyright 2018 IQIYI
#    Author:   Bean
#    Contact:  guhaibin1847@gmail.com
"""
    数学计算工具
"""
import numpy as np


def mape(y_true_arr, y_pred_arr):
    return np.mean(np.abs((np.array(y_true_arr) - np.array(y_pred_arr)) / np.array(y_true_arr))) * 100


def r_square(y_true_arr, y_pred_arr):
    y_bar = sum(y_true_arr) / len(y_true_arr)
    # sse = np.sum(np.square(np.array(y_true_arr) - np.array(y_pred_arr)))
    sse = sum([(x - y) ** 2 for x, y in zip(y_true_arr, y_pred_arr)])
    sst = sum([(y - y_bar) ** 2 for y in y_true_arr])
    return 1 - sse / sst

def fba(y_true_arr, y_pred_arr): # 业务方的准确率标准
    y = np.append(y_pred_arr, y_true_arr) # 把预测值和实际值合成一个一维数组
    y = y.reshape((2, len(y_true_arr))).transpose() # 将这个一维数组变为二维数组并转置 
    output_accuracy = np.array(list(map(lambda x : np.min(x) / np.max(x), y))) # 计算每个业务准确率
    return np.average(output_accuracy)
    