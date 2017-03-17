import Individual

def getEvolution(pop_size, ind_size, generation, problem, pop=[]):

    for i in range(pop_size):
        pop.append(Individual(ind_size))
    print ('the population is ', len(pop), 'individuals')

    ### evaluate population
    new_pop = pop
    for i in new_pop:
        walkability(i)
        structure(i)
    hamming_dist(new_pop)

    ### Pareto front for each generation will be stored in this list
    pareto_fronts_out = []
    ### Values for individuals in pareto front for each gen will be stored in this list
    values_out = []
    ### Full pop will be stored here
    full_pop_out = []

    ### Evolution starts here
    while generation > 0:
        ### sort population
        fronts = sort_pop(new_pop, problem)
        sorted_pop = [ind for front in fronts for ind in front]

        ### elite population
        e_pop = []
        for ind in sorted_pop:
            if ind not in e_pop and len(e_pop) < int(len(new_pop) / 4):
                e_pop.append(ind)

        ### mating pool
        m_pool = tournament(sorted_pop, len(new_pop) - len(e_pop), problem)

        ### operate on mating pool
        off_1 = mate(m_pool)
        offspring = mutate(off_1, 0.05)

        ### recompose population
        new_pop = e_pop + offspring
        for ind in new_pop:
            ind.clear_values()

        ### re_evaluate new_pop
        for i in new_pop:
            walkability(i)
            structure(i)
        hamming_dist(new_pop)
        fronts2 = sort_pop(new_pop, problem)
        pFront = fronts[0]
        pFront2 = []
        for ndf in pFront:
            if ndf not in pFront2:
                pFront2.append(ndf)
        pareto_fronts_out.append(pFront2)
        values_out.append([i.values for i in pFront2])
        srtd_pop = [ind for front in fronts2 for ind in front]
        full_pop_out.append(srtd_pop)
        generation -= 1
    print 'there are ', len(full_pop_out), 'in the pareto front'
    print pareto_fronts_out
    print values_out
    print full_pop_out
    prompt1 = raw_input('Terminate? (Y/N): ')
    if prompt1 == 'Y':
        exit()
        # print 'there are ', len(full_pop_out), 'in the pareto front'
        # return pareto_fronts_out, values_out, full_pop_out
    elif prompt1 == 'N':
        # _pop_size = pop_size
        # _ind_size = ind_size
        # _gens = gens
        # _problem = problem
        #TODO using try/except statement
        prompt2 = raw_input('seed population (enter list of indice up to %s): '
                            % (len(full_pop_out[0]) - 1))
        seed_pop = [
            full_pop_out[-1][seeded_ind]
            for seeded_ind in [int(ii) for ii in prompt2.split(',')]
        ]
        print 'you have selected', len(seed_pop), 'individuals to seed next gen'
        return evolve(pop_size, ind_size, _gens, problem, seed_pop)
    else:
        return 'You have failed!'
#
# if __name__ == "__main__":
#     evolve(100, (2,3,4), 10, 'max')

def Accessibility(ind):

