#!/usr/bin/env python3

from email.errors import MisplacedEnvelopeHeaderDefect
from algo1 import hopcroft_karp, maximal_alternating_sequence, algorithm_one, run_with_time
import numpy as np 

@run_with_time
def algorithm_two(X,Y, e, example_name):


    # use algo1 and hopcroft_karp output to calculate M[x_l, y_l]
    
    matchings, _ = hopcroft_karp(X,Y,e)
    subset_dict, n_for_tc, m_for_tc, _, step_count, _ = algorithm_one(X,Y,e)
    # print(algorithm_one(X,Y,e))
    x_l, y_l = subset_dict["x_l"], subset_dict["y_l"]
    
    # filter matchings based on them containing vertices in x_l and y_l 
    matched_x_vertices = [m[0] for m in matchings if m[0] in x_l]
    matched_y_vertices = [m[1] for m in matchings if m[1] in y_l]

    step_count += 1
    return [m for m in matchings if m[0] in matched_x_vertices and m[1] in matched_y_vertices], n_for_tc, m_for_tc, example_name, step_count, "Algorithm Two"


# print(algorithm_two(['A','B','C','D'], ['E','F','G','H'], np.array([[1,1,0,1], [1,0,1,1], [0,0,0,1], [1,0,0,1]]), example_name="Example One"))
# print(algorithm_two(['A','B','C','D','E','F','G','H'], ['Z','Y','X','W','V','U','T'],
#                  np.array([[1,0,1,0,1,0,0,0], [0,1,0,1,0,1,0,0], [0,1,0,0,1,1,1,0], 
#                           [0,0,1,1,1,1,0,1], [0,0,0,0,0,0,1,0], [0,0,0,0,0,0,0,1], 
#                           [0,0,0,0,0,0,0,1]]), example_name="Example Two"))
# print(algorithm_two(['A','B','C','D'], ['J','K','L'], np.array([[0,0,1,0],[1,1,0,0],[0,0,1,1]]), example_name='Example Three'))