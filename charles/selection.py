from random import uniform, sample, random, choice
from operator import attrgetter
import numpy as np

def tournament(population, size=5):

    """
    Tournament selection method
    Args:
        population: The population from which the selection method will act.
    Returns: an individual
    """

    # 'tourn_ind' is a variable that stores the individuals selected to take part in the selection method

    tourn_ind = sample(population.individuals, size) # used sample instead of choice to don't allow replacement
    #tourn_ind = [choice(population.individuals) for i in range(size)]

    if population.optim == "max":
        return max(tourn_ind, key=attrgetter("fitness"))

    elif population.optim == "min":
        return min(tourn_ind, key=attrgetter("fitness"))
    else:
        raise Exception("No optimization specified (min or max).")

def fps(population):
    """Fitness proportionate selection implementation.

    Args:
        population: The population from which the selection method will act.

    Returns:
        Individual: selected individual.
    """

    if population.optim == "max":
        # total_fitness stores the sum of all fitness
        total_fitness = sum([i.fitness for i in population])
        # Get a 'position' on the wheel
        spin = uniform(0, total_fitness)
        position = 0
        # Find individual in the position of the spin
        for individual in population:
            position += individual.fitness
            if position > spin:
                return individual

    elif population.optim == "min":
        # adapted from https://rocreguant.com/roulette-wheel-selection-python/2019/
        # Sum total fitnesses
        total_fitness = sum([i.fitness for i in population])

        # Computes for each individual, its probability
        indiv_probabilities = [i.fitness / total_fitness for i in population]

        # Making the probabilities for a minimization problem
        indiv_probabilities = 1 - np.array(indiv_probabilities)

        # Selects one individual accordingly to 'indiv_probabilities'
        return np.random.choice(population, p=indiv_probabilities)

    else:
        raise Exception("No optimization specified (min or max).")

def rank (population):
    """
    Rank selection

    Args:
        population: The population from which the selection method will act.

    Returns:
        Individual: selected individual.
    """
    # Sort individuals according to the optimization choice
    if population.optim == "max":
        population.individuals.sort(key=attrgetter("fitness"))
    elif population.optim == "min":
        population.individuals.sort(key=attrgetter("fitness"), reverse=True)
    else:
        raise Exception("No optimization specified (min or max).")

    # get the sum of all ranks
    total = sum(range(population.size_pop + 1))
    # Get a random spin
    spin = uniform(0, total)
    position = 0

    #  Find individual in the position of the spin
    for count, individual in enumerate(population):
        position += count + 1
        if position > spin:
            return individual
