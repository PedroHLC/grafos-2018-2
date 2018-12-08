#!/usr/bin/env python
import networkx as nx
import numpy as np

A = np.loadtxt('./input/ha30_dist.txt')
G = nx.from_numpy_matrix(A)

T = []
# Nossa raiz será o nó '0'
U = [0]

def aresta_valida(e):
    v, u, data = e
    return (v in U) and (u not in U)

def pega_peso(e) :
    _, _, data = e
    return data['weight']

def menor_aresta_restante():
    return sorted(filter(aresta_valida, G.edges(data=True)), key=pega_peso)

while True:
    k = menor_aresta_restante()
    if(len(k) < 1):
        break;
    # É interessante pra gente somente a cabeça, descartamos a calda
    e, *_ = k
    # É interessante somente o vértice de destino, descartamos a origem e a data
    _, v, _ = e
    T.append(e)
    U.append(v)

print(T)

ArvoreGerMin = nx.create_empty_copy(G)
for v,u,data in T:
    ArvoreGerMin.add_edge(v, u, data=data)
from matplotlib import pyplot
nx.draw_networkx(ArvoreGerMin)
pyplot.show()