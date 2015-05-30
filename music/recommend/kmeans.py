__author__ = 'jjzhu'
__doc__ = 'K-均值聚类支持'

import numpy as np
from math import *
from pylab import *
import time

color_list = ['red', 'blue', 'yellow', 'green', 'black', 'black', 'black']


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
        #     scatter(centroids[cent, 0], centroids[cent, 1], c='black')
        #     annotate(u'旧中心点'+str(cent), xy=(centroids[cent, 0], centroids[cent, 1]),
        #              xytext=(centroids[cent, 0]-2, centroids[cent, 1]-2), fontsize=12,
        #              arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
        #     centroids[cent, :] = np.mean(cluster, axis=0)  # 更新族中心
        # #
        #     scatter(cluster[:, 0], cluster[:, 1], c=color_list[cent])
        #     scatter(centroids[cent, 0], centroids[cent, 1], c='black', label='cluster'+str(cent))
        #     annotate(u'新中心点'+str(cent), xy=(centroids[cent, 0], centroids[cent, 1]),
        #              xytext=(centroids[cent, 0]-2, centroids[cent, 1]-2), fontsize=12,
        #              arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
        # legend(loc='upper left')
        # show()
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
        # ylim(-8, 8)
        # for i in range(len(center_list)):
        #     cluster_mat = data_set[np.nonzero(cluster_ss[:, 0].A == i)[0], :]
        #     scatter(cluster_mat[:, 0], cluster_mat[:, 1], c=color_list[i], label='cluster'+str(i))
        # for i in range(len(center_list)):
        #
        #     scatter(np.mat(center_list)[i, 0], np.mat(center_list)[i, 1], c=color_list[i], marker='*')
        #     annotate(u'中心点'+str(i), xy=(np.mat(center_list)[i, 0], np.mat(center_list)[i, 1]),
        #              xytext=(np.mat(center_list)[i, 0]-2, np.mat(center_list)[i, 1]-2), fontsize=12,
        #              arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
        # legend(loc='upper left')
        # show()
        # time.sleep(2)
        lowest_sse = np.inf  # 最小误差平方和
        for i in range(len(center_list)):
            # 获取属于当前簇的向量
            current_cluster_index = data_set[np.nonzero(
                cluster_ss[:, 0].A == i)[0], :]
            if current_cluster_index.__len__() == 0:
                continue
            centroid_mat, split_cluster_ss = kmeans(
                current_cluster_index, 2, dist_measure)

            for j in range(3):
                temp_centroid_mat, temp_cluster = kmeans(
                    current_cluster_index, 2, dist_measure)
                if np.sum(temp_cluster[:, 1]) < np.sum(split_cluster_ss[:, 1]):
                    centroid_mat, split_cluster_ss = temp_centroid_mat, temp_cluster
            # 获取当前划分簇的误差平方和
            sse_of_split = np.sum(split_cluster_ss[:, 1])
            # 计算为被划分的误差
            sse_of_not_split = np.sum(
                cluster_ss[np.nonzero(cluster_ss[:, 0].A != i)[0], 1])

            if (sse_of_split + sse_of_not_split) < lowest_sse:
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


# 计算轮廓系数
def sc(data_set, cluster_result, k):
    all_sc = 0.
    for i in range(k):
        curr_cluster = data_set[np.nonzero(cluster_result[:, 0].A == i)[0]]
        n = np.shape(curr_cluster)[0]
        for j in range(n):
            b_i = np.inf
            dist_sum = 0.
            for t in range(n):
                dist_sum += dist_eclud(curr_cluster[j], curr_cluster[t])
            a_i = dist_sum/n-1
            for p in range(k):
                if p != i:
                    curr_out_cluster = data_set[np.nonzero(cluster_result[:, 0].A == p)[0]]
                    if np.shape(curr_out_cluster)[0] == 0:
                        continue
                    out_dist_sum = 0.
                    for point in range(np.shape(curr_out_cluster)[0]):
                        out_dist_sum += dist_eclud(curr_cluster[j], curr_out_cluster[point])
                    curr_bi = out_dist_sum/np.shape(curr_out_cluster)[0]
                    if curr_bi < b_i:
                        b_i = curr_bi
            all_sc += (b_i - a_i)/np.max([a_i, b_i])
        print(all_sc)
        return all_sc/np.shape(data_set)[0]


# 加载测试数据集
def load_data_set(file_name):
    data_mat = []  # 数据矩阵
    file_read = open(file_name)  # 打开文件
    for line in file_read.readlines():
        cur_line = line.strip().split('\t')  # tab 分割
        float_line = list(map(float, cur_line))  # 类型转换
        data_mat.append(float_line)
    return data_mat


def test1():
    # data_mat = np.mat(load_data_set('data/testSet.txt'))
    # centroids, cluster_assment = kmeans(data_mat, 2)
    # print(centroids)
    # print(cluster_assment)
    # print('---------------------------------------------')
    data_set = np.mat(load_data_set('data/kmeans/testSet2.txt'))
    # 画图
    ylim(-8, 8)
    scatter(data_set[:, 0].flatten().A[0], data_set[:, 1].flatten().A[0], c='blue', label=u'待聚类数据集', linewidths=1,)
    legend(loc='upper left')
    show()
    x = []
    y = []
    for k in range(2, 8):
        center_list, cluster_ss = binary_kmeans(data_set, k)
        ylim(-8, 8)
        for i in range(k):
            cluster_mat = data_set[np.nonzero(cluster_ss[:, 0].A == i)[0], :]
            scatter(cluster_mat[:, 0], cluster_mat[:, 1], c=color_list[i], label='cluster'+str(i))
        for i in range(len(center_list)):
            scatter(np.mat(center_list)[i, 0], np.mat(center_list)[i, 1], c=color_list[i], marker='*')
            annotate(u'中心点'+str(i), xy=(np.mat(center_list)[i, 0], np.mat(center_list)[i, 1]),
                     xytext=(np.mat(center_list)[i, 0]-2, np.mat(center_list)[i, 1]-2), fontsize=12,
                     arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
        legend(loc='upper left')
        print(sc(data_set, cluster_ss, k))
        x.append(k)
        y.append(sc(data_set, cluster_ss, k))
        show()
    plot(x, y)
    show()


    # print(centroids)
    # print(cluster_assment)
    # print(cluster_assment)
    # print(dist_eclud(data_mat[0], data_mat[1]))


def test2():
    data_set = np.mat(load_data_set('data/kmeans/testSet.txt'))
    centroids, cluster_ss = kmeans(data_set, 4)
    print("test2")

if __name__ == '__main__':
    test1()
