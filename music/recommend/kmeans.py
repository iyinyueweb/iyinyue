__author__ = 'jjzhu'
__doc__ = 'K-均值聚类支持'

import numpy as np
from math import *


# 计算两个向量的欧式距离
def dist_eclud(vector_a, vector_b):
    return sqrt(np.sum(np.power(vector_a - vector_b, 2)))


# 初始化族心
def random_center(data_set, k):
    n = np.shape(data_set)[1]  # 获取输入矩阵维度
    centroids = np.mat(np.zeros((k, n)))  # k * n 阶矩阵
    for i in range(n):
        min_value = min(data_set[:, i])  # 获取索引为i的向量
        # 计算向量的极值之差
        range_value = float(max(data_set[:, i]) - min_value)  
        # 随机获取并保存质心
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
    # cluster_ss[i, 0]存储向量i的族心向量索引
    # cluster_ss[i, 1]存储向量i与族心向量的距离
    cluster_ss = np.mat(np.zeros((m, 2)))
    centroids = create_center(data_set, k)  # 随机获取K个族心
    cluster_changed = True  # 族心改变标识
    while cluster_changed:
        cluster_changed = False
        for i in range(m):
            min_dist = np.inf  # np.inf = +无穷大
            min_index = -1  # 族心向量索引
            for j in range(k):
                # 计算两个向量的距离
                vector_dist = dist_measure(centroids[j, :], data_set[i, :])  
                if vector_dist < min_dist:  # 计算距离哪个族向量最近
                    min_dist = vector_dist  # 记录距离
                    min_index = j  # 记录族向量索引
            if cluster_ss[i, 0] != min_index:  # 判断族中心是否改变
                cluster_changed = True
                cluster_ss[i, :] = min_index, min_dist ** 2  # 更新族心索引与距离
        # 更新族心位置
        for cent in range(k):
            cluster = data_set[np.nonzero(cluster_ss[:, 0].A == cent)[0]]  
            centroids[cent, :] = np.mean(cluster, axis=0)  # 更新族中心
    return centroids, cluster_ss


# 二分k-means算法
# 克服了k-means算法收敛于局部最小值的问题
# 基本思路：
#   将所有点都看成一个簇
#   当簇数< K时：
#       对每一个簇
#           计算总误差
#           在给定的簇上在进行k-means聚类（K=2)
#           计算将该簇一分为二的总误差
#       选择使得误差最小的那个簇进行划分操作
def binary_kmeans(data_set, k, dist_measure=dist_eclud):
    m = np.shape(data_set)[0]
    cluster_ss = np.mat(np.zeros((m, 2)))  # 初始化一个m * 2 阶矩阵
    centroid0 = np.mean(data_set, axis=0).tolist()[0]  # 创建簇心
    center_list = [centroid0]
    for i in range(m):
        cluster_ss[i, 1] = dist_measure(
            np.mat(centroid0), data_set[i, :]) ** 2  # 计算各点距簇中心的距离
    while len(center_list) < k:
        lowest_sse = np.inf  # 最小误差平方和
        for i in range(len(center_list)):
            # 获取属于当前簇的向量
            current_cluster_index = data_set[np.nonzero(
                cluster_ss[:, 0].A == i)[0], :]
            centroid_mat, split_cluster_ss = kmeans(
                current_cluster_index, 2, dist_measure)  # 二分聚类
            # 获取当前划分簇的误差平方和
            sse_of_split = np.sum(split_cluster_ss[:, 1])
            # 计算为被划分的误差
            sse_of_not_split = np.sum(
                cluster_ss[np.nonzero(cluster_ss[:, 0].A != i)[0], 1])
            if sse_of_split + sse_of_not_split < lowest_sse:
                # 若一分为二的总误差小于最小误差
                best_center_to_split_index = i  # 记录最佳划分索引
                best_new_centroids = centroid_mat  # 记录最佳划分中心
                best_cluster_ss = split_cluster_ss.copy()  # 记录最佳划分后的平方和
                lowest_sse = sse_of_split + sse_of_not_split  # 更新最小误差平方和
        # 更新所属簇
        best_cluster_ss[np.nonzero(
            best_cluster_ss[:, 0].A == 1)[0], 0] = len(center_list)
        best_cluster_ss[np.nonzero(best_cluster_ss[:, 0].A == 0)[0], 0] = \
            best_center_to_split_index
        # 用第一个划分替换当前的划分点
        center_list[best_center_to_split_index] =\
            best_new_centroids[0, :].tolist()[0]
        center_list.append(best_new_centroids[1, :].tolist()[0])  # 添加第二个划分中心
        # 更新当前划分簇的误差平方和
        cluster_ss[np.nonzero(
            cluster_ss[:, 0].A == best_center_to_split_index)[0], :] = best_cluster_ss
    return np.mat(center_list), cluster_ss


# 加载测试数据集
def load_data_set(file_name):
    data_mat = []  # 数据矩阵
    file_read = open(file_name)  # 打开文件
    for line in file_read.readlines():
        cur_line = line.strip().split('\t')  # tab 分割
        float_line = list(map(float, cur_line))  # 类型转换
        data_mat.append(float_line)
    return data_mat


def test():
    # data_mat = np.mat(load_data_set('data/testSet.txt'))
    # centroids, cluster_assment = kmeans(data_mat, 2)
    # print(centroids)
    # print(cluster_assment)
    # print('---------------------------------------------')
    data_mat = np.mat(load_data_set('data/testSet2.txt'))
    centroids, cluster_assment = binary_kmeans(data_mat, 3)
    print(centroids)
    # print(cluster_assment)
    # print(dist_eclud(data_mat[0], data_mat[1]))

if __name__ == '__main__':
    test()
