#!/usr/bin/env python3
from .algo1 import algorithm_one, hopcroft_karp, run_with_time


@run_with_time
def algorithm_two(X,Y, e, example_name=None):
    """Our implementation of algorithm 2.

    Args:
        X (list): x components (columns in the array representation) of bipartite graph (G)
        Y (list): y components (rows in the array representation) of bipartite graph (G)
        e (np.array): 2D array representation of G (1 = edge, 0 = no edge)
        example_name (str, optional): Name of the instance. Defaults to None.

    Returns:
        dict({"x_l":x_l, "x_s":x_s, "y_l":y_l, "y_s":y_s}) (dict): dict of lists and the name of that list of vertices 
            either contained in or not contained in the max alternating sequence.
    """
    # use algo1 and hopcroft_karp output to calculate M[x_l, y_l]
    
    matchings, _ = hopcroft_karp(X,Y,e)
    subset_dict, n_for_tc, m_for_tc, _, step_count, _ = algorithm_one(X,Y,e)
    x_l, y_l = subset_dict["x_l"], subset_dict["y_l"]
    
    # filter matchings based on them containing vertices in x_l and y_l 
    matched_x_vertices = [m[0] for m in matchings if m[0] in x_l]
    matched_y_vertices = [m[1] for m in matchings if m[1] in y_l]

    step_count += 1
    return [m for m in matchings if m[0] in matched_x_vertices and m[1] in matched_y_vertices], n_for_tc, m_for_tc, example_name, step_count, "Algorithm Two"
