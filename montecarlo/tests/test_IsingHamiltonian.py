import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
import math

# needed this import format to access the functions in the package
from montecarlo.BitString import *
from montecarlo.compute_average_values import *
from montecarlo.IsingHamiltonian import *

def test_IsingHamiltonian():
    """"
    This tests the IsingHamiltonian class and a compute_average_values
    """
    # create graph 
    G = nx.Graph()
    G.add_nodes_from([i for i in range(12)])
    G.add_edges_from([(i,(i+1)% G.number_of_nodes() ) for i in range(12)])
    G.add_edge(1,7)
    G.add_edge(4,9)
    for i in G.edges:
        G.edges[i]['weight'] = 1.5

    # create inputs
    J = [[] for i in G.nodes()]
    for i in G.edges: # forgot to actually add to the J list
        J[i[0]].append((i[1], G.edges[i]['weight']))
        J[i[1]].append((i[0], G.edges[i]['weight']))
    mus = np.zeros(len(G.nodes()))
    # mus = np.zeros(0)
    bs = BitString(8)
    bs.set_int_config(12)

    ham = IsingHamiltonian(J, mus)

    E, M, HC, MS = ham.compute_average_values(1)

    #verifies the values from the internal compute_average_values
    assert(round(E, 5) == -16.33200)
    assert(round(M, 5) == 0.00000)
    assert(round(HC, 5) == 3.46899)
    assert(round(MS, 5) == 1.03298)