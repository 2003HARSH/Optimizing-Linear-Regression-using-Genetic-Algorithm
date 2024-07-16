import random
import numpy as np

class Dna:
    def __init__(self) -> None:
        self.param=random.random()

    @staticmethod
    def crossover(parent1,parent2):
        return np.array([parent1[0],parent2[1]])

    @staticmethod
    def mutation(child,mutation_rate,mutation_scale,):        
        if random.random() < mutation_rate:
            child[0] += random.random()*mutation_scale

        if random.random() < mutation_rate:
            child[0] -= random.random()*mutation_scale

        if random.random() < mutation_rate:
            # child[1] += random.gauss(0, mutation_scale)
            child[1] += random.random()*mutation_scale

        if random.random() < mutation_rate:
            child[1] -= random.random()*mutation_scale

        return child