from random import choice, random
import numpy as np
from copy import deepcopy
from operator import attrgetter

class Individual:
    def __init__(
                self,
                representation=None,
                initial_sudoku=None,
                valid_set=[i for i in range(1, 10)]):

        self.index_missing = [i for i in range(len(initial_sudoku)) if initial_sudoku[i] == 0]
        if initial_sudoku is None:
            raise Exception(
                "It is mandatory to provide an initial sudoku."
            )

        #if isinstance(np.sqrt(len(initial_sudoku)), float):# check if it ia a square
        #    raise Exception(
        #        "The Sudoku's size must be the square of an integer number."
        #    )

        if representation == None:
            #If a representation is not assigned, a possible solution is generated
            new_sudoku = deepcopy(initial_sudoku)
            # For each row
            for j in np.arange(0, 81, 9):
                number_missing = deepcopy(valid_set)
                for i in range(j, j+9):  # indexes for each 'row'
                    if i not in self.index_missing:# removing the numbers given from a list of possible numbers to fill
                        number_missing.remove(initial_sudoku[i])
                for i in range(j, j+9):
                    if i in self.index_missing:
                        new_sudoku[i] = choice(number_missing) #assigning a random number for each missing value (0)
                        number_missing.remove(new_sudoku[i])
            self.representation = deepcopy(new_sudoku)





        else: #if representation is defined by the user
            self.representation = representation

        self.fitness = self.get_fitness()

    def get_fitness(self):
        raise Exception("You need to monkey patch the fitness path.")

    def get_neighbours(self, func, **kwargs):
        raise Exception("You need to monkey patch the neighbourhood function.")

    def __len__(self):
        return len(self.representation)

    def __getitem__(self, position):
        return self.representation[position]

    def __setitem__(self, position, value):
        self.representation[position] = value

    def __repr__(self):
        return f"Individual(size={len(self.representation)}); Fitness: {self.fitness}"

class Population:
    def __init__(self, initial_sudoku, size_pop, optim, **kwargs):
        self.individuals = []
        self.size_pop = size_pop
        self.optim = optim
        self.initial_sudoku = initial_sudoku
        self.gen = 1

        for _ in range(size_pop):
            self.individuals.append(
                Individual(
                    initial_sudoku=initial_sudoku,
                    # size=kwargs["sol_size"], #### ver ####
                    valid_set=kwargs["valid_set"], #### ver ####
                )
            )

    def evolve(self, gens, select, crossover, mutate, co_p, mu_p, elitism):
        for gen in range(gens):
            new_pop = []

            if elitism == True:
                if self.optim == "max":
                    elite = deepcopy(max(self.individuals, key=attrgetter("fitness")))
                elif self.optim == "min":
                    elite = deepcopy(min(self.individuals, key=attrgetter("fitness")))

            while len(new_pop) < self.size_pop:
                parent1, parent2 = select(self), select(self)
                # Crossover
                if random() < co_p:
                    offspring1, offspring2 = crossover(parent1, parent2)
                else:
                    offspring1, offspring2 = parent1, parent2
                # Mutation
                if random() < mu_p:
                    offspring1 = mutate(offspring1)
                if random() < mu_p:
                    offspring2 = mutate(offspring2)

                new_pop.append(Individual(representation=offspring1))
                print(new_pop)
                if len(new_pop) < self.size:
                    new_pop.append(Individual(representation=offspring2))

            if elitism == True:
                if self.optim == "max":
                    least = min(new_pop, key=attrgetter("fitness"))
                elif self.optim == "min":
                    least = max(new_pop, key=attrgetter("fitness"))
                new_pop.pop(new_pop.index(least))
                new_pop.append(elite)

            self.individuals = new_pop

            if self.optim == "max":
                print(f'Best Individual: {max(self, key=attrgetter("fitness"))}')
            elif self.optim == "min":
                print(f'Best Individual: {min(self, key=attrgetter("fitness"))}')
