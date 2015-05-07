__author__ = 'jjzhu'

import numpy as np


def pca(data_mat, top_n=9999999):
    mean_values = np.mean(data_mat, axis=0)  # 求平均值
    mean_removed = data_mat - mean_values
    cov_mat = np.cov(mean_removed, rowvar=0)
    eig_values, eig_vectors = np.linalg.eig(cov_mat)  # 求特征值和特征向量
    eig_value_index = np.argsort(eig_values)  # 升序排序返回位置索引
    eig_value_index = eig_value_index[: -(top_n + 1): -1]  # 排序结果逆序
    top_n_vectors = eig_vectors[:, eig_value_index]
    low_d_data_mat = mean_removed * top_n_vectors  # 降维
    new_mat = (low_d_data_mat * top_n_vectors.T) + mean_values
    return low_d_data_mat, new_mat


def load_data_set(file_name, delim='\t'):
    fr = open(file_name)
    string_arr = [line.strip().split(delim) for line in fr.readlines()]
    data_arr = [list(map(float, line)) for line in string_arr]
    return np.mat(data_arr)

if __name__ == '__main__':
    data_mat = load_data_set('../data/pca/testSet.txt')
    # print(data_mat)
    low_d_data, new_mat = pca(data_mat, 1)
    print(low_d_data)
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(data_mat[:, 0].flatten().A[0], data_mat[:, 1].flatten().A[0], marker='^', s=90)
    ax.scatter(new_mat[:, 0].flatten().A[0], new_mat[:, 1].flatten().A[0], marker='o', s=50, c='red')
    plt.show()
