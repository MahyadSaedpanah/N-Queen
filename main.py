from parameters import *
from initial_population import init_Population
from cross_over import cross_over
from mutation import mutation
from fitness import fitness
from presentation import show

current_population = init_Population(N, PS)
urrent_population = fitness(current_population, N)
current_population = sorted(current_population, key=lambda x:x[-1])
if current_population[0][-1]==0:
    print("Solution is found in the initail population stage", current_population[0])
    show(current_population[0],N)
else:
    for i in range (EPOCH):
        current_population = cross_over(current_population, N, PS)
        current_population = mutation(current_population, N, PS, MR)
        current_population = fitness(current_population, N)
        current_population = sorted(current_population, key=lambda x:x[-1])
        current_population = current_population[:PS]   #delete
        if current_population[0][-1]==0:
            print(i+1,"Solution found:",current_population[0])
            show(current_population[0],N)
            break
        else:
            print(i+1,"Best solution so far:",current_population[0])
    else:
        print("Sorry, We could not find you a solution!")