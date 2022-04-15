#!/usr/bin/env python3

from email.errors import MisplacedEnvelopeHeaderDefect
from algo1 import hopcroft_karp, maximal_alternating_sequence, algorithm_one
import numpy as np 

def algorithm_two(X,Y, e):
    # use algo1 and hopcroft_karp output to calculate M[x_l, y_l]
    
    matchings = hopcroft_karp(X,Y,e)
    subset_dict = algorithm_one(X,Y,e)

    x_l, y_l = subset_dict["x_l"], subset_dict["y_l"]

    # filter matchings based on them containing vertices in x_l and y_l 
    matchings_with_x = [m for m in matchings if m[0] in x_l]
    matchings_with_y = [m for m in matchings if m[1] in y_l]

    return [m for m in matchings if m in matchings_with_x or m in matchings_with_y]

print(algorithm_two(['A','B','C','D'], ['E','F','G','H'], np.array([[1,1,0,1], [1,0,1,1], [0,0,0,1], [1,0,0,1]])))