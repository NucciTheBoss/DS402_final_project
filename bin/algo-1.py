


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
        e (np.array): 2D array of matchings (1 = matching, 0 = no matching)

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

hopcroft_karp(['A','B','C','D'], ['E','F','G','H'], np.array([[1,1,0,1], [1,0,1,1], [0,0,0,1], [1,0,0,1]]))

def algorithm_one(X, Y, e):
    """_summary_

    Args:
        x (list): x components of bipartite graph (G)
        y (list): y components of bipartite graph (G)
        e (np.array): set of matchings (matching is a set of edges without common vertices)

    Returns:
        _type_: _description_
    """
    x_not = []
    max_card_matching = hopcroft_karp(X,Y,e)
    for x in X:
        if x not in [m[0] for m in max_card_matching]:
            x_not.append(x)

    # compute maximal M-alternating sequence S(max_card_matching, x_not)
    

    return None
    









"""
    copy_dict = e
    M = [] # initialize matchings to be null
    boolean = True
    # while boolean: 
    matched_vertices_x = []
    matched_vertices_y = []
    free_vertices = []
    P = []
    # Using BFS, build alternating level graph, rooted at unmatched vertices in set X
    # for x in X: 
    #     # find all matchings that each x in X has within e
    #     if x not in matched_vertices_x:
    #         edges = e.get(x)
    #         # print(edges)
    #         for _ in edges: 
    #             if _ not in free_vertices:
    #             # and _ not in matched_vertices_y:
    #                 free_vertices.append(_)
    
    free_vertices = list(np.unique([i for i in list(itertools.chain(*copy_dict.values()))]))
    for y_vertex in free_vertices:  
        x_vertex = [i for i,j in copy_dict.items() if y_vertex in j]
        if x_vertex != [] and x_vertex not in matched_vertices_x:
            copy_dict.pop(x_vertex[0])   
            free_vertices.remove(y_vertex)
            # matching = str(x_vertex[0]+ "-"+y_vertex)
            # print(x_vertex, matching)
             
            matched_vertices_x.append(x_vertex[0])
            matched_vertices_y.append(y_vertex)
            
            matching = str(x_vertex[0]+ "-"+y_vertex)
            P.append(matching)
    #         # remove all connections to y_vertex 
    #         for key in copy_dict.keys():
    #             print(key)
    #             print([y for y in copy_dict[key] if y not in matched_vertices_y])
    print(copy_dict)
    print(P)
    # print(copy_dict)               
    # print(P)
    #     # print(P)
    #     # M = set(M) ^ set(P)
    #     # print(M)
    #     # if len(free_vertices) == 0:
    #     #     boolean = False
    #     # else:
    #     #     boolean = True
        

    # return M
"""
