from random import randint as rnd

def init_Population(n, ps):
    population_list = []
    for i in range(ps):
        member = []
        for j in range(n):
            member.append(rnd(0,n-1))
        population_list.append(member+[None])
    return population_list