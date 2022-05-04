#!/usr/bin/python3
from typing import Any, List, Tuple, Union

import numpy as np
from flask import Flask, jsonify, request

from bin.algo1 import algorithm_one
from bin.algo2 import algorithm_two


# Globals
app = Flask(__name__)


def _parse(pref: Union[Any, None]) -> Tuple[List, List, np.array]:
    """Parse preference packet sent by client.

    Args:
        pref (Union[Any, None]): User preferences as a JSON packet.

    Returns:
        Tuple[List, List, np.array]: Tuple containing agents, objects, and an array symbolizing
        which object they are pointing to.
    """
    
    # Construct agent preferences list
    agent_preferences = []
    for item in pref.values():
        agent = []
        agent.append(item["name"])
        agent.append(item["preferences"].split("->"))
        agent_preferences.append(agent)

    # Construct agent list
    agent_list = [agent[0] for agent in agent_preferences]

    # Construct object list
    object_list = []
    for agent in agent_preferences:
        for object in agent[1]:
            if object not in object_list:
                object_list.append(object)


    # Contrust numpy array representing agent preferences
    pref_graph = []
    for object in object_list:
        object_pref = []
        for agent in agent_preferences:
            if object in agent[1]:
                object_pref.append(1)
            else:
                object_pref.append(0)

        pref_graph.append(object_pref)

    return agent_list, object_list, np.array(pref_graph)


@app.route("/algo1", methods=["GET"])
def algo1_response():
    if request.method == "GET":
        data = request.get_json()
        pref = _parse(data)
        algorithm_one(pref[0], pref[1], pref[2], "Server Test")
    
    return jsonify({"status": "200"})
    


@app.route("/algo2", methods=["GET"])
def algo2_response():
    if request.method == "GET":
        data = request.get_json()
        pref = _parse(data)
        algorithm_two(pref[0], pref[1], pref[2], "Server Test")

    return jsonify({"status": "200"})
    


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
