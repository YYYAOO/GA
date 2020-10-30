from translateDNA_def import translateDNA
from fx import F
import numpy as np

def get_fitness(pop, DNA_SIZE, X_BOUND, Y_BOUND):
    x, y = translateDNA(pop, DNA_SIZE, X_BOUND, Y_BOUND)
    pred = F(x, y)
    return (pred - np.min(pred))  # 减去最小的适应度是为了防止适应度出现负数，通过这一步fitness的范围为[0, np.max(pred)-np.min(pred)]
