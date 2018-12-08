#!/usr/bin/env python
import networkx as nx
import sys

G = nx.read_pajek( './input/'+
    ('dolphins' if (sys.argv[1] == '1') else 'karate')
    +'.paj'
    )

def DFS_recursivo(G, predecessores, descobertos, raiz):
    print(len(descobertos))
    for v in G.neighbors(raiz):
        if v not in descobertos:
            descobertos.append(v)
            predecessores[v] = raiz
            predecessores, descobertos = DFS_recursivo(G, predecessores, descobertos, v)

    return predecessores, descobertos

def DFS_completo(G, raiz):
    predecessores = {}
    for v in G.nodes():
        predecessores[v] = None

    predecessores, descobertos = DFS_recursivo(G, predecessores, [raiz], raiz)
    print(predecessores)
    print(descobertos)

    ArvoreBFS = nx.create_empty_copy(G)
    for v,u,data in G.edges(data=True):
        if(predecessores[u] is v) or (predecessores[v] is u):
            ArvoreBFS.add_edge(v, u, data=data)

    return ArvoreBFS

from matplotlib import pyplot
nx.draw_networkx(DFS_completo(G, ('0' if (sys.argv[1] == '1') else '1')))
pyplot.show()