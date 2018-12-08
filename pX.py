#!/usr/bin/env python
import networkx as nx
import numpy as np

A = [[0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]]

raiz = 0
fim = 5

G = nx.from_numpy_matrix(np.matrix(A), create_using=nx.MultiDiGraph())

def fordfulkerson():
    for _,_,data in G.edges(data=True):
        data['fuk'] = 0