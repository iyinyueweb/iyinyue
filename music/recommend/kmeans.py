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
    return sqrt(np.sum(np.power(vector_a - vector_b, 2)))


# 初始化族心
def random_center(data_set, k):
    n = np.shape(data_set)[1]  # 获取输入矩阵维度
    centroids = np.mat(np.zeros((k, n)))  # k * n 阶矩阵
    for i in range(n):
        min_value = min(data_set[:, i])
        range_value = float(max(data_set[:, i]) - min_value)
        centroids[:, i] = min_value + range_value * np.random.rand(k, 1)  # 编译器提示找不到rand方法直接忽略
    return centroids


# kmeans聚类函数
# param：
#   data_set: 带聚类数据向量集
#   k ： 待聚类的类别数
#   dist_measure: 计算两个向量的距离，默认是欧式向量计算
#   create_center: 随机初始化族心方法，默认的是rangdo_center
def kmeans(data_set, k, dist_measure=dist_eclud, create_center=random_center):
    m = np.shape(data_set)[0]  # 获取矩阵行数

    # 创建一个 m * 2的矩阵 用于记录向量所属族心
    # cluster_assment[i, 0]存储向量i的族心向量索引
    # cluster_assment[i, 1]存储向量i与族心向量的距离
    cluster_assment = np.mat(np.zeros((m, 2)))
    centroids = create_center(data_set, k)  # 随机获取K个族心
    cluster_changed = True  # 族心改变标识
    while cluster_changed:
        cluster_changed = False
        for i in range(m):
            min_dist = np.inf  # np.inf = +无穷大
            min_index = -1  # 族心向量索引
            for j in range(k):
                vector_dist = dist_measure(centroids[j, :], data_set[i, :])  # 计算两个向量的距离
                if vector_dist < min_dist:  # 计算距离哪个族向量最近
                    min_dist = vector_dist  # 记录距离
                    min_index = j  # 记录族向量索引
            if cluster_assment[i, 0] != min_index:  # 判断族中心是否改变
                cluster_changed = True
                cluster_assment[i, :] = min_index, min_dist ** 2  # 更新族心索引与距离
        # 更新族心位置
        for cent in range(k):
            cluster = data_set[np.nonzero(cluster_assment[:, 0].A == cent)[0]]  # 取出同一族的向量集合
            centroids[cent, :] = np.mean(cluster, axis=0)  # 计算族中心
    return centroids, cluster_assment


def test():
    data_mat = np.mat(load_data_set('data/testSet.txt'))
    centroids, cluster_assment = kmeans(data_mat, 2)
    print(centroids)
    print(cluster_assment)
    # print(dist_eclud(data_mat[0], data_mat[1]))

if __name__ == '__main__':
    test()
