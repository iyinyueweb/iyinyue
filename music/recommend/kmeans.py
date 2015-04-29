__author__ = 'jjzhu'
__doc__ = 'K-均值聚类支持'

import numpy as np
from math import *


# 加载测试数据集
def load_data_set(file_name):
    data_mat = []  # 数据矩阵
    file_read = open(file_name)  # 打开文件
    for line in file_read.readlines():
        cur_line = line.strip().split('\t')  # tab 分割
        float_line = list(map(float, cur_line))  # 类型转换
        data_mat.append(float_line)
    return data_mat


# 计算两个向量的欧式距离
def dist_eclud(vector_a, vector_b):
    return sqrt(sum(np.power(vector_a - vector_b, 2)))


# 初始化族心
def random_center(data_set, k):
    n = np.shape(data_set)[1]  # 获取输入矩阵维度
    centroids = np.mat(np.zeros((k, n)))  # k * n 阶矩阵
    for i in range(n):
        min_value = min(data_set[:, i])
        range_value = float(max(data_set[:, i]) - min_value)
        centroids[:, i] = min_value + range_value * np.random.rand(k, 1)
    return centroids


def test():
    data_mat = np.mat(load_data_set('data/testSet.txt'))
    print(random_center(data_mat, 2))
    print(np.power(data_mat[0] - data_mat[1], 2))
    # print(dist_eclud(data_mat[0], data_mat[1]))

if __name__ == '__main__':
    test()
