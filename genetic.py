# genetic algorithm search for continuous function optimization
from numpy.random import randint
from numpy.random import rand
from graph import Graph


# tournament selection
def selection(pop, scores, k=3):
    """
    pick k tournaments and pick the best parent in each call
    best is determined by scores array (fitness scores (based on objective function))
    """
    # first random selection
    selection_ix = randint(len(pop))
    for ix in randint(0, len(pop), k - 1):
        # check if better (e.g. perform a tournament)
        if scores[ix] > scores[selection_ix]:
            selection_ix = ix
    return pop[selection_ix]


# crossover two parents to create two children
def crossover(p1, p2, r_cross):
    """
    r_cross (crossover rate) is a hyperparameter that determines whether crossover is performed or not,
    and if not, the parents are copied into the next generation (default behaviour in this case)
    It is a probability and typically has a large value close to 1.0.
    """
    # children are copies of parents by default
    c1, c2 = p1.copy(), p2.copy()
    # check for recombination
    if rand() < r_cross:
        # select crossover point that is not on the end of the string
        pt = randint(1, len(p1) - 2)
        # perform crossover
        """
        one-point crossover
        """
        c1 = p1[:pt] + p2[pt:]
        c2 = p2[:pt] + p1[pt:]
    return [c1, c2]


# mutation operator
def mutation(bitstring, r_mut):
    """
    mutate bitstring itself, NOT the copy
    """
    for i in range(len(bitstring)):
        # check for a mutation
        if rand() < r_mut:
            # flip the bit
            """
            bit-flip mutation
                1 - (1) => 0
                1 - (0) => 1
            """
            bitstring[i] = 1 - bitstring[i]


# genetic algorithm
def genetic_algorithm(graph, n_bits, n_iter, n_pop, r_cross, r_mut):
    # initial population of random bitstring
    

    pop = [randint(0, 2, n_bits).tolist() for _ in range(n_pop)]
    """
    pop =>
    [
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0]
        ...
        ...
        ...
        (n_pop)th array
    ]
    """

    # keep track of best solution

    graph.gen_to_graph(pop[0])

    best, best_eval = 0, graph.index_per()

    # enumerate generations
    for gen in range(n_iter):
        # decode population
        scores = []

        for p in pop:
            graph.remove_all_edges()
            graph.gen_to_graph(p)
            scores.append(graph.index_per())

        # check for new best solution
        for i in range(n_pop):
            if scores[i] < best_eval:
                best, best_eval = pop[i], scores[i]
                print(">%d, new best = %f" % (gen, scores[i]))

        # select parents
        selected = [selection(pop, scores) for _ in range(n_pop)]
        # `selected` is a length 100 array of each element being 32 length arrays

        # create the next generation
        children = list()
        for i in range(0, n_pop, 2):
            # get selected parents in pairs
            p1, p2 = selected[i], selected[i + 1]
            # crossover and mutation
            for c in crossover(p1, p2, r_cross):
                # mutation
                mutation(c, r_mut)
                # store for next generation
                children.append(c)

        # replace population
        pop = children

    return [best, best_eval]

# define the total iterations
n_iter = 100
# bits per variable
n_bits = 10
# define the population size
n_pop = 100
# crossover rate: high probability value
r_cross = 0.9
# mutation rate: low probability value
r_mut = 1.0 / float(n_bits) 
# perform the genetic algorithm search

g = Graph()

g.add_vertex('1')
g.add_vertex('2')
g.add_vertex('3')
g.add_vertex('4')
g.add_vertex('5')


best, score = genetic_algorithm(
    g, n_bits, n_iter, n_pop, r_cross, r_mut
)
# getting the best population and the best score possible
print("Done!")

for v in g:
    for w in v.get_connections():
        vid = v.get_id()
        wid = w.get_id()
        print ('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))

