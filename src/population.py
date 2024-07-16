import random
import numpy as np
from src.dna import Dna

class Population:
    def __init__(self,population_size,number_of_parameters,mutation_rate) -> None:
        self.population_size=population_size
        self.mutation_rate=mutation_rate
        self.number_of_parameters=number_of_parameters
        self.best_score=0
        self.best_param=[]
        self.generation=0
    
    def generate_population(self):
        l=np.random.rand(self.population_size,self.number_of_parameters)
        return l

    def calculate_fitness(self,population_list,X,Y):
        fitness_scores=[]
        for i in range(len(population_list)):
            y_pred=population_list[i][0]*X+population_list[i][1]
            total_error=(1/len(Y))*np.sum((Y-y_pred)**2)
            fitness_scores.append(1/total_error)

        return fitness_scores

    def natural_selection(self,population_list,fitness_scores,mating_pool_length):
        mating_pool=[]
        self.best_score=max(fitness_scores)
        inde=fitness_scores.index(self.best_score)
        self.best_param=population_list[inde]


        for i in range(mating_pool_length):
          ele=max(fitness_scores)
          ind=fitness_scores.index(ele)
          app_ele=population_list[ind]
          mating_pool.append(app_ele)
          population_list.pop(ind)
          fitness_scores.pop(ind)

        if len(mating_pool)==0:
            mating_pool=population_list
        return mating_pool

    def generate_new_population(self,mating_pool,mutation_scale):
        new_population=[]
        for i in range(self.population_size):           
            parent1=np.array(mating_pool[random.randrange(0,len(mating_pool))])
            parent2=np.array(mating_pool[random.randrange(0,len(mating_pool))])
            child=Dna.crossover(parent1,parent2)
            new_child=Dna.mutation(child,self.mutation_rate,mutation_scale)
            new_population.append(new_child.tolist())
        return new_population