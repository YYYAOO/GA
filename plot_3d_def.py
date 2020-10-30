import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from fx import F

def plot_3d(ax, X_BOUND, Y_BOUND):  # 绘制3d图
    X = np.linspace(*X_BOUND, 100)
    Y = np.linspace(*Y_BOUND, 100)
    X, Y = np.meshgrid(X, Y)  # 从坐标向量中返回坐标矩阵
    Z = F(X, Y)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm)
    ax.set_zlim(-10, 10)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.pause(3)
    plt.show()
