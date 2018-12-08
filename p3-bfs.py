#!/usr/bin/env python
import networkx as nx
import sys

G = nx.read_pajek( './input/'+
    ('dolphins' if (sys.argv[1] == '1') else 'karate')
    +'.paj'
    )

def BFS(G, raiz):
    predecessores = {}
    for v in G.nodes():
        predecessores[v] = None
    
    descobertos = [raiz]
    F = [raiz]
    
    while F:
        u = F.pop(0)
        for v in G.neighbors(u):
            if v not in descobertos:
                predecessores[v] = u
                descobertos.append(v)
                F.append(v)

    ArvoreBFS = nx.create_empty_copy(G)
    for v,u,data in G.edges(data=True):
        if(predecessores[u] is v) or (predecessores[v] is u):
            ArvoreBFS.add_edge(v, u, data=data)

    return ArvoreBFS

from matplotlib import pyplot
nx.draw_networkx(BFS(G, ('0' if (sys.argv[1] == '1') else '1')))
pyplot.show()