
from copy import deepcopy
from charles.charles import Population, Individual
from initial_puzzle import easy, medium, hard
from charles.selection import fps, tournament, rank
from charles.crossover import uniform_co_alt, uniform_co
from charles.mutation import mutation_sample, mutation_prob, mutation_swap
import numpy as np

def get_fitness(self):
    """ This function computes fitness scores of each individual (a possible solution).
       Since it considers the number of unique digits in each row, column and box, the maximum fitness is 243 (81*3)

       Returns:
           fitness_value (int): the fitness for a sudoku solution
    """

    # initializing and declaring a variable that will store the fitness value of a solution
    fitness_value = 0

    # get rows' fitness
    for row in np.arange(0, 81, 9):
        fitness_value += len(set(self.representation[row:row+9]))

    # get columns' fitness
    for columns in range(0, 9):
        column_evaluate = []
        for elem in [index + columns for index in np.arange(0, 81, 9)]:
            column_evaluate.append(self.representation[elem])
        fitness_value += len(set(column_evaluate))

    # get boxs' fitness
    # creating these variables to make the code susceptible to different Sudoku sizes
    #base = len(self.representaion)**(1/4)  # 3
    #len_box = base ** 2  # 9
    #len_line_box = len_box * base  # 27

    base=3
    len_box=9
    len_line_box=27

    for k in range(0, base):

            #first 3 blocks, second  blocks, third three blocks
            box_partial = deepcopy(self.representation)
            box_partial = box_partial[k*len_line_box : k*len_line_box+len_line_box]
            for i in range(0, base):# for each block
                    box = []
                    for j in range(0, base): #for each line of the block
                            box.append(box_partial[j*len_box + i*base : j*len_box + i*base+base])
                    box = [x for sublist in box for x in sublist]
                    fitness_value += len(set(box))

    return fitness_value

# the neighborhood does not apply for this specific problem
def get_neighbours (self):
    pass

# monkey patching
Individual.get_fitness = get_fitness
Individual.get_neighbours = get_neighbours

pop_easy = Population(size_pop=20, optim="max", initial_sudoku=easy, valid_set=[i for i in range(1, 10)])

pop_easy.evolve(gens=100, select=tournament, crossover=uniform_co_alt, mutate=mutation_swap, co_p=0.9, mu_p=0.1, elitism=False)