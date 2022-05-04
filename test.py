#!/usr/bin/python3
import unittest

import numpy as np

from bin.algo1 import (algorithm_one, hopcroft_karp,
                       maximal_alternating_sequence)
from bin.algo2 import algorithm_two


class TestHopcroftKarp(unittest.TestCase):
    def test_hopcroft(self):
        print(hopcroft_karp(['A','B','C','D'], ['E','F','G','H'], np.array([[1,1,0,1], [1,0,1,1], [0,0,0,1], [1,0,0,1]])))
        print(hopcroft_karp(['A','B','C','D','E','F','G','H'], ['Z','Y','X','W','V','U','T'],
                        np.array([[1,0,1,0,1,0,0,0], [0,1,0,1,0,1,0,0], [0,1,0,0,1,1,1,0], 
                                [0,0,1,1,1,1,0,1], [0,0,0,0,0,0,1,0], [0,0,0,0,0,0,0,1], 
                                [0,0,0,0,0,0,0,1]])))
        print(hopcroft_karp(['A','B','C','D'], ['J','K','L'], np.array([[0,0,1,0],[1,1,0,0],[0,0,1,1]])))


class TestMaximalAlternatingSequence(unittest.TestCase):
    def test_maximal_alternating_sequence(self):
        maximal_alternating_sequence(['A','B','C','D','E','F','G','H'], ['Z','Y','X','W','V','U','T'],
                        np.array([[1,0,1,0,1,0,0,0], [0,1,0,1,0,1,0,0], [0,1,0,0,1,1,1,0], 
                                [0,0,1,1,1,1,0,1], [0,0,0,0,0,0,1,0], [0,0,0,0,0,0,0,1], 
                                [0,0,0,0,0,0,0,1]]), matchings=['AZ', 'BY', 'HU', 'EX', 'CW', 'GV'], step_count=0, verts_to_check=['F','D'])
        maximal_alternating_sequence(['A','B','C','D'], ['J','K','L'], np.array([[0,0,1,0],[1,1,0,0],[0,0,1,1]]), matchings=['CJ', 'DL', 'AK'], step_count=0, verts_to_check=['B'])


class TestAlgoOne(unittest.TestCase):
    def test_algo_one(self):
        print(algorithm_one(['A','B','C','D'], ['E','F','G','H'], np.array([[1,1,0,1], [1,0,1,1], [0,0,0,1], [1,0,0,1]]), example_name="Example One"))
        print(algorithm_one(['A','B','C','D','E','F','G','H'], ['Z','Y','X','W','V','U','T'],
                        np.array([[1,0,1,0,1,0,0,0], [0,1,0,1,0,1,0,0], [0,1,0,0,1,1,1,0], 
                                [0,0,1,1,1,1,0,1], [0,0,0,0,0,0,1,0], [0,0,0,0,0,0,0,1], 
                                [0,0,0,0,0,0,0,1]]), example_name="Example Two"))
        print(algorithm_one(['A','B','C','D'], ['J','K','L'], np.array([[0,0,1,0],[1,1,0,0],[0,0,1,1]]), example_name='Example Three'))


class TestAlgoTwo(unittest.TestCase):
    def test_algo_two(self):
        print(algorithm_two(['A','B','C','D'], ['E','F','G','H'], np.array([[1,1,0,1], [1,0,1,1], [0,0,0,1], [1,0,0,1]]), example_name="Example One"))
        print(algorithm_two(['A','B','C','D','E','F','G','H'], ['Z','Y','X','W','V','U','T'],
                        np.array([[1,0,1,0,1,0,0,0], [0,1,0,1,0,1,0,0], [0,1,0,0,1,1,1,0], 
                                [0,0,1,1,1,1,0,1], [0,0,0,0,0,0,1,0], [0,0,0,0,0,0,0,1], 
                                [0,0,0,0,0,0,0,1]]), example_name="Example Two"))
        print(algorithm_two(['A','B','C','D'], ['J','K','L'], np.array([[0,0,1,0],[1,1,0,0],[0,0,1,1]]), example_name='Example Three'))
