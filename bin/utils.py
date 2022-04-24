import pandas as pd
import time
from datetime import datetime
import 


def run_with_time(func):
    def wf(*args, **kwargs):
        stime = time.time()
        result, n, m, algorithm_name, example_name = func(*args, **kwargs) # may need to adjust this to handle the differing for each variables time complexity
        etime = time.time()
        # send data to function to save runtime results 
        runtime_df = add_to_csv(file="runtime.csv", additions=[algorithm_name, example_name, n, m, etime-stime])
        
        # return/save an updated graph after adding the information to the runtime file 
        
        return result 
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
        # print(df)
        df = pd.DataFrame(new_df)
        df.to_csv(file, index=False)
        # update the file to contain the additions
        # df.to_csv(file, index=False)
        return df
    else:
        return df




def generate_runtime_graph(file, algorithm):
    """Generates and saves a graph to compare runtime for algorithm with expected runtime

    Args:
        file (_type_): _description_
    """
    # contains expected/theoretical runtime for each algorithm
    algo_runtime = {"One":[], "Two":[], "Three":[], "Four":[]}