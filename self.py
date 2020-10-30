import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from fx import F
from get_fitness_def import get_fitness
from crossover_and_mutation_def import crossover_and_mutation
from mutation_def import mutation
from translateDNA_def import translateDNA
from select_def import select
from print_info_def import print_info
from plot_3d_def import plot_3d

DNA_SIZE = 24  # x、y各取12位，位数越高，越精确
POP_SIZE = 200  # 种群规模
CROSSOVER_RATE = 0.8  # 交叉概率
MUTATION_RATE = 0.005  # 变异概率
N_GENERATIONS = 50  # 迭代次数
X_BOUND = [-3, 3]  # x取值区间
Y_BOUND = [-3, 3]  # y取值区间

if __name__ == "__main__":
    fig = plt.figure()
    ax = Axes3D(fig)
    plt.ion()  # 将画图模式改为交互模式，程序遇到plt.show不会暂停，而是继续执行
    plot_3d(ax, X_BOUND, Y_BOUND)

    # 初始种群，二进制
    pop = np.random.randint(2, size=(POP_SIZE, DNA_SIZE * 2))
    # low (inclusive) to high (exclusive)的随机整数，默认high=None，则取[0, low)
    # 种群迭代N代
    for _ in range(N_GENERATIONS):
        x, y = translateDNA(pop, DNA_SIZE, X_BOUND, Y_BOUND)  # 二进制翻译为十进制

        if 'sca' in locals():
            sca.remove()
        sca = ax.scatter(x, y, F(x, y), c='black', marker='o');
        plt.show();
        plt.pause(0.1)

        fitness = get_fitness(pop, DNA_SIZE, X_BOUND, Y_BOUND)  # 适应度函数值
        pop = select(pop, fitness, POP_SIZE)  # 选择 生成新的种群
        pop = np.array(crossover_and_mutation(pop, CROSSOVER_RATE, POP_SIZE, DNA_SIZE))  # 交叉

    print_info(pop, DNA_SIZE, X_BOUND, Y_BOUND)
    plt.ioff()
    plot_3d(ax, X_BOUND, Y_BOUND)
