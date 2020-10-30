from get_fitness_def import get_fitness
from translateDNA_def import translateDNA
import numpy as np

def print_info(pop, DNA_SIZE, X_BOUND, Y_BOUND):
    fitness = get_fitness(pop, DNA_SIZE, X_BOUND, Y_BOUND)
    max_fitness_index = np.argmax(fitness)
    print("max_fitness:", fitness[max_fitness_index])
    x, y = translateDNA(pop, DNA_SIZE, X_BOUND, Y_BOUND)
    print("最优的基因型：", pop[max_fitness_index])
    print("(x, y):", (x[max_fitness_index], y[max_fitness_index]))