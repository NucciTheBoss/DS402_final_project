#!/usr/bin/python3
import math
import os

import pandas as pd
from matplotlib import pyplot as plt


def run_with_time(func):
    def wf(*args, **kwargs):
        # may need to adjust this to handle the differing for each variables time complexity
        result, n, m, example_name, steps, algorithm_name = func(*args, **kwargs)
        
        # send data to function to save runtime results
        # overwrites 
        file = 'runtime.csv'
        df = pd.read_csv(file)
        df1 = pd.DataFrame([[algorithm_name, example_name, n, m, steps]], 
            columns=['Algorithm Name','Example Name','N','M','Run Time'])
        
        df.append(df1).to_csv(file, index=False)

        return result, n, m, example_name, steps, algorithm_name 
    return wf


def add_to_csv(file, additions):
    """
        Adds new information to file (in the specific instance new information is new runtime data collected)

    Args:
        file (csv file): file to add 
        additions (list): list of additions to insert into the file
            - etime = additions[0]
            - x_var = additions[1]
    Return:
        None
    """
    
    df = pd.read_csv(file)
    if additions[1] not in df["Example Name"].values:
        new_df = {"Algorithm Name":[additions[0]],
                "Example Name":additions[1],
                "N":[additions[2]], 
                "M":[additions[3]],
                "Run Time":[additions[4]]}
        df = pd.DataFrame(new_df)
        df.to_csv(file, index=False)
        # update the file to contain the additions
        # df.to_csv(file, index=False)
        return df
    else:
        return df




def generate_runtime_graph(file, algorithm, mode):
    """Generates and saves a graph to compare runtime for algorithm with expected runtime

    Args:
        file (_type_): _description_
    """
    
    df = pd.read_csv(file) 
    algo_df = df[df['Algorithm Name'] == algorithm]

    if algorithm == "Algorithm 1" and mode=="Time Complexity":
        # create a new column of the expected max runtime 
        algo_df["Time Complexity"] = [algo_df["M"][i]*math.sqrt(algo_df["N"][j]) for i in range(len(algo_df["M"].astype("float32"))) 
                        for j in range(len(algo_df["N"].astype("float32"))) if i == j]
    
    if algorithm == "Algorithm 2" and mode=="Time Complexity":
        algo_df["Time Complexity"] = [algo_df["M"].values[i]*algo_df["N"].values[j] + algo_df["N"].values[j]**2 * math.log(algo_df["N"].values[j]) 
                        for j in range(len(algo_df["N"])) for i in range(len(algo_df["M"])) if j == i]
    # find data necessary for graphing 
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')

    x = algo_df['M'].values
    y = algo_df['N'].values
    z = algo_df[mode].values

    ax.set_xlabel("N Value")
    ax.set_ylabel("M Value")
    if algorithm == "Algorithm 1":
        ax.set_zlabel("Number steps")
    if algorithm == "Algorithm 2":
        ax.set_zlabel("Number steps")

    ax.scatter(x,y,z, color='red', marker='o')

    for i in range(len(x)):
        # annotate the points for easier representation 
        txt = "({},{},{})".format(x[i], y[i], z[i])
        ax.text(x[i],y[i],z[i], txt)
    

    plt.savefig(os.path.join("Graphs", algorithm + mode + "_graph.png"))
    
# generate_runtime_graph("runtime.csv", "Algorithm 1","Run Time")
# # generate_runtime_graph("runtime.csv", "Algorithm 1","Time Complexity")
# generate_runtime_graph("runtime.csv", "Algorithm 2", "Run Time")
# # generate_runtime_graph("runtime.csv", "Algorithm 2", "Time Complexity")

