"""
Test to verify energy function
"""

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
import math
from montecarlo.BitString import *
from montecarlo.energy import *

def test_energy():
    # establish energy inputs
    bs = BitString(8)
    bs.set_int_config(8)
    G = nx.Graph()
    G.add_nodes_from([i for i in range(8)])
    G.add_edges_from([(i,(i+1)% G.number_of_nodes() ) for i in range(8)])
    G.add_edge(1,7)
    for e in G.edges:
        G.edges[e]['weight'] = 1.0


    # define the current energy and assert value
    eng = energy(bs,G)
    assert(eng == 5.0)