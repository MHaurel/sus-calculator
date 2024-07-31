import pandas as pd

def calculate_sus_per_individual(individual_row):
    sum_ = 0
    for index, rating in enumerate(individual_row):
        iindex = index + 1
        if iindex % 2 == 1: # if index is odd
            sum_ += int(rating) - 1
        else: # in the other case
            sum_ += (5 - int(rating))
    return sum_*2.5

def calculate_sus(sus):
    global_score = 0
    nb_individuals = len(sus.index)
    for i in range(nb_individuals):
        sus_score = calculate_sus_per_individual(sus.iloc[i].values)
        global_score += sus_score

    return global_score / nb_individuals