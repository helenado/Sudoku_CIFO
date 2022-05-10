from random import sample, random
import numpy as np
from random import choice
from copy import deepcopy


def no_mutation(indiv):
    """
    """

    return indiv

def mutation_sample(indiv, number_mut=3):
    """
    """

    indexes_mut = sample(indiv.index_missing, k=number_mut)[0] # used sample instead of choices because of the non 'replacement' factor

    for i in indexes_mut:
        indiv[i] = sample([i for i in range(1, 10)], k=1)[0] ## VER

    return indiv

def mutation_prob(indiv, prob):
    """
    """
    for i in indiv.index_missing:
        if random() < prob:
            indiv[i] = sample(indiv.valid_set, k=1)
    return indiv

def mutation_swap(indiv):

    """
    """
    random_decision = sample(range(0, 3), k=1)[0]

    if random_decision == 0: #do mutation by rows

        ind_chosen = sample(range(0, 9), k=1)[0] * 9
        missing_row = list(set(indiv.index_missing).intersection(set(range(ind_chosen, ind_chosen+9))))
        choose_2 = sample(missing_row, k=2)
        indiv_orig = deepcopy(indiv)
        indiv[choose_2[0]] = indiv[choose_2[1]]
        indiv[choose_2[1]] = indiv_orig[choose_2[0]]

    elif random_decision == 1: # do mutation by columns

        ind_chosen = sample(range(0, 9), k=1)[0]
        ind_column = [ind_chosen+(i*9) for i in range(0, 9)]
        missing_column = list(set(indiv.index_missing).intersection(set(ind_column)))
        choose_2 = sample(missing_column, k=2)

        indiv_orig = deepcopy(indiv)
        indiv[choose_2[0]] = indiv[choose_2[1]]
        indiv[choose_2[1]] = indiv_orig[choose_2[0]]

    elif random_decision == 2:
        block_chosen = sample(range(0, 3), k=1)[0]
        box_chosen = sample(range(0, 3), k=1)[0]

        ind_initial = block_chosen*27 + box_chosen*3
        missing_box = []
        for k in range(0, 3): # 3 lines

            ind_box = [ind_initial+i + k*9 for i in range(0, 3)]

            missing_box = missing_box + list(set(indiv.index_missing).intersection(set(ind_box)))

        choose_2 = sample(missing_box, k=2)

        indiv_orig = deepcopy(indiv)
        indiv[choose_2[0]] = indiv[choose_2[1]]
        indiv[choose_2[1]] = indiv_orig[choose_2[0]]


    return indiv


def mutation_swap_all (indiv):
    """
    """
    random_decision = sample(range(0, 3), k=1)[0]

    if random_decision == 0:  # do mutation by rows

        ind_chosen = sample(range(0, 9), k=1)[0] * 9
        missing_row = list(set(indiv.index_missing).intersection(set(range(ind_chosen, ind_chosen + 9))))

        missing_sampled = sample(missing_row, len(missing_row))

        indiv_orig = deepcopy(indiv)

        for i in range(len(missing_row)):

            indiv[missing_row[i]] = indiv_orig[missing_sampled[i]]

    elif random_decision == 1:  # do mutation by columns

        ind_chosen = sample(range(0, 9), k=1)[0]

        ind_column = [ind_chosen + (i * 9) for i in range(0, 9)]
        missing_column = list(set(indiv.index_missing).intersection(set(ind_column)))

        missing_sampled = sample(missing_column, len(missing_column))

        indiv_orig = deepcopy(indiv)

        for i in range(len(missing_column)):
            indiv[missing_column[i]] = indiv_orig[missing_sampled[i]]

    elif random_decision == 2:
        block_chosen = sample(range(0, 3), k=1)[0]
        box_chosen = sample(range(0, 3), k=1)[0]

        ind_initial = block_chosen * 27 + box_chosen * 3
        missing_box=[]
        for k in range(0, 3):  # 3 lines
            ind_box = []
            ind_box = [ind_initial + i + k * 9 for i in range(0, 3)]
            missing_box = missing_box + list(set(indiv.index_missing).intersection(set(ind_box)))

        missing_sampled = sample(missing_box, len(missing_box))

        indiv_orig = deepcopy(indiv)

        for i in range(len(missing_box)):
            indiv[missing_box[i]] = indiv_orig[missing_sampled[i]]

    return indiv


