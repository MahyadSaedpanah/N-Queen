def cross_over(population_list, n, ps):
    for i in range(0,ps,2):
        child2 = population_list[i+1][:n//2]+population_list[i][n//2:n]+[None]
        child1 = population_list[i][:n//2]+population_list[i+1][n//2:n]+[None]
        population_list.append(child1)
        population_list.append(child2)
    return population_list