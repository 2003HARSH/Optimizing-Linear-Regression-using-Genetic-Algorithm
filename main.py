import numpy as np
from src.population import Population


X=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
m=5
c=10
Y=m*X+c
ppl=Population(100,2,0.5)
ppl_list=ppl.generate_population()
mutation_scale=0.1*(max(X)-min(X))

for i in range(20):
    print("\n\n#######################################\n\n")
    fitness=ppl.calculate_fitness(ppl_list,X,Y)
    for j in range(len(ppl_list)):
        print("Generation : ",i,"\t NN_params [weight,bias] : ",ppl_list[j],"\tFitness Score :",fitness[j])
    mating_pool=ppl.natural_selection(ppl_list.tolist(),fitness,2)
    new_ppl_list=ppl.generate_new_population(mating_pool,mutation_scale)

    ppl_list=np.array(new_ppl_list)

    print("\n\nMost fit Neural Network : ",ppl.best_param,"\tBest Fitness Score : ",ppl.best_score,"\n\n")
