import numpy as np


# 将二进制的染色体基因型编码成十进制的表现型。
def translateDNA(pop, DNA_SIZE, X_BOUND, Y_BOUND):
    # pop表示种群矩阵，一行表示一个二进制编码表示的DNA，矩阵的行数为种群数目
    x_pop = pop[:, 1::2]  # 第一个维度都取，第二个维度上的奇数列表示x
    y_pop = pop[:, ::2]  # 第二个维度上的偶数列表示y

    # dot()返回的是两个数组的点积(dot product)，x_pop与（）的点积
    # arange()中有一个参数表示默认起点0，步长为1 输出：[0 1 ... n]
    # x_pop.dot(2 ** np.arange(DNA_SIZE)[::-1])  二进制->十进制，按权重展开
    # x_pop.dot(2 ** np.arange(DNA_SIZE)[::-1]) / float(2 ** DNA_SIZE - 1)  将转换后的实数压缩到 [0,1]之间的一个小数

    # 映射为x范围内的数，由二进制还原为十进制
    x = x_pop.dot(2 ** np.arange(DNA_SIZE)[::-1]) / float(2 ** DNA_SIZE - 1) * (X_BOUND[1] - X_BOUND[0]) + X_BOUND[0]
    # 映射为y范围内的数
    y = y_pop.dot(2 ** np.arange(DNA_SIZE)[::-1]) / float(2 ** DNA_SIZE - 1) * (Y_BOUND[1] - Y_BOUND[0]) + Y_BOUND[0]
    return x, y
