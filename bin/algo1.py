


# links 
# https://www.youtube.com/watch?v=lM5eIpF0xjA
# https://www.youtube.com/watch?v=CSUEVu-qUgM
# https://www.youtube.com/watch?v=0GNYjXUPTFM
# 

import numpy as np
import copy
import itertools
from more_itertools import locate 

def hopcroft_karp(X,Y,e):
    """_summary_

    Args:
        x (list): x components (columns in the array representation) of bipartite graph (G)
        y (list): y components (rows in the array representation) of bipartite graph (G)
        e (np.array): 2D array representation of G (1 = edge, 0 = no edge)

    Returns:
        M (list): list of maximum cardinality matching found
    """ 
    num_x_vertices = len(X)
    num_y_vertices = len(Y)

    M = []

    matched_y_vertices = []
    matched_x_vertices = []
    
    condition = True
    while condition == True:
        copy_arr = copy.deepcopy(e)
        p = []
        free_vertices = []
        
        # build free_vertices list
        for i in range(num_x_vertices):
            for j in range(num_y_vertices):
                # find the value in the array for the matching
                m = copy_arr[i][j]
                if m == 1: 
                    if j not in free_vertices:
                        # add the vertice to free_vertices
                        free_vertices.append(j)
        
        free_vertices.sort() # sorts the free_vertices according to the original input list Y
        # BFS on free_vertices 
        for y_vertex in free_vertices:
            if y_vertex not in matched_y_vertices:
            # look at that row, find the first occurence of 1 
                if len(M) == 0:
                    if 1 in copy_arr[y_vertex]:
                        x_index_for_matching_w_y_vertex = copy_arr[y_vertex].tolist().index(1)
                        matched_x_vertices.append(x_index_for_matching_w_y_vertex)
                        matched_y_vertices.append(y_vertex)
                        p.append([y_vertex, x_index_for_matching_w_y_vertex])
                        # remove connections to both y_vertex
                        copy_arr[y_vertex] = 0
                        # remove connections to x_vertex 
                        copy_arr[:,x_index_for_matching_w_y_vertex] = 0
                        
                    continue 
                        
                else: # M is populated so must be past 1st iteration
                    # find vertices in X set that connect to unmatched edge in y (y_vertex)
                    x_indices_for_matching_w_y_vertex = list(locate(copy_arr[y_vertex]))
                    for x_v in x_indices_for_matching_w_y_vertex:
                        # build the matching to y 
                        matching_w_y = [y_vertex, x_v]
                        for mtch in M:
                            if str(x_v) == mtch[-1]:                            
                                # now check e row for connection to unmapped x vertice 
                                for _ in X:
                                    if X.index(_) not in matched_x_vertices and copy_arr[int(mtch[0])][X.index(_)] == 1:
                                        # there is a match and it can be added to p
                                        p.append(matching_w_y)
                                        p.append([int(mtch[0]), int(mtch[-1])])
                                        p.append([int(mtch[0]), X.index(_)])
                                        matched_x_vertices.append(X.index(_))
                                        matched_y_vertices.append(y_vertex)

                        break        
        
        p_for_xoring = ["-".join([str(c) for c in lst]) for lst in p]
        M = list(set(M) ^ set(p_for_xoring))

        if len(p) == 0:
            condition = False
        else:
            condition = True
    
    cleaned_m = [str(X[int(i[-1])] + Y[int(i[0])]) for i in M]
    # print(cleaned_m)
    return cleaned_m

# print(hopcroft_karp(['A','B','C','D'], ['E','F','G','H'], np.array([[1,1,0,1], [1,0,1,1], [0,0,0,1], [1,0,0,1]])))





def maximal_alternating_sequence(X, Y, e, matchings, verts_to_check, sequences=[]):
    """_summary_

    Args:
        X (list): x components of bipartite graph (G)
        Y (list): y components of bipartite graph (G)
        e (np.array): set of matchings (matching is a set of edges without common vertices)
        verts_to_check (list): vertices (in X or Y) to be checked in order to find the next set of
        e_without_matchings (np.array): 2D array of e with edges included in matchings removed (None until creation in first pass)
        sequences (list): list containing strings of all sequences created

    Returns:
        max(sequences, key=len) (string): longest string in sequences
    """

    e_without_matchings = copy.deepcopy(e)
    for match in matchings:
        # find indices need to remove these edges in e 
        x_index = X.index(match[0])
        y_index = Y.index(match[1])
        e_without_matchings[y_index, x_index] = 0

    e_with_only_matchings = np.zeros(e.shape)
    for match in matchings:
        # find indices need to remove these edges in e 
        x_index = X.index(match[0])
        y_index = Y.index(match[1])
        e_with_only_matchings[y_index, x_index] = 1
    
    if verts_to_check[0] in X:
        finding = "Y"
    else:
        finding  = "X"
    # build sets, start with Y_i given X_0
    for v in verts_to_check:
        if finding == "X":
            connections_to_y = list(locate(e_with_only_matchings[Y.index(v)]))
            # build alternating sequence with each v and  
            if len(connections_to_y) == 0:
                # no further connections (i.e. termination condition of {})
                return max(sequences, key=len)
            else:
                sequences = [str(v + "-" + X.index(i)) for i in connections_to_y]
                # iterate through again with new found vertices
                new_verts_to_check = [X.index(i) for i in connections_to_y]
                maximal_alternating_sequence(X, Y, e, matchings, verts_to_check=new_verts_to_check, sequences=sequences)
        else:
            connections_to_x = list(locate(e_without_matchings[:, X.index(v)]))
            if len(connections_to_x) == 0:
                # no further connections (i.e. termination condition of {})
                return max(sequences, key=len)
            else:
                sequences = [str(v + "-" + Y.index(i)) for i in connections_to_x]
                # iterate through again with new found vertices
                new_verts_to_check = [Y.index(i) for i in connections_to_x]
                maximal_alternating_sequence(X, Y, e, matchings, verts_to_check=new_verts_to_check,sequences=sequences)

# maximal_alternating_sequence(['A','B','C','D'], ['E','F','G','H'], np.array([[1,1,0,1], [1,0,1,1], [0,0,0,1], [1,0,0,1]]), matchings=['CF', 'BE', 'AH', 'DG']

def algorithm_one(X, Y, e):
    """_summary_

    Args:
        x (list): x components of bipartite graph (G)
        y (list): y components of bipartite graph (G)
        e (np.array): set of matchings (matching is a set of edges without common vertices)

    Returns:
        dict({"x_l":x_l, "x_s":x_s, "y_l":y_l, "y_s":y_s}) (dict): dict of lists and the name of that list of vertices 
            either contained in or not contained in the max alternating sequence
    """
    x_not = []
    max_card_matching = hopcroft_karp(X,Y,e)
    for x in X:
        if x not in [m[0] for m in max_card_matching]:
            x_not.append(x)
    
    # compute maximal M-alternating sequence S(max_card_matching, x_not)
    # can be more than one vertice in x_not, so for loop through it; 
    # also can be empty if all x vertices are matched
    if len(x_not) == 0:
        # then none of the vertices participate in the set as they are all matched
        x_l, y_l, x_s, y_s = X, Y, [], [] 
        
        return dict({"x_l":x_l, "x_s":x_s, "y_l":y_l, "y_s":y_s})
        
    else:
        # compute maximal alternating sequence
        mas = maximal_alternating_sequence(X, Y, e, matchings=max_card_matching, verts_to_check=x_not)

        x_l, y_l, x_s, y_s = [i for i in X if i not in mas], [j for j in Y if j not in mas], [q for q in X if q in mas], [z for z in Y if z in mas]
        return dict({"x_l":x_l, "x_s":x_s, "y_l":y_l, "y_s":y_s})        

# print(algorithm_one(['A','B','C','D'], ['E','F','G','H'], np.array([[1,1,0,1], [1,0,1,1], [0,0,0,1], [1,0,0,1]])))