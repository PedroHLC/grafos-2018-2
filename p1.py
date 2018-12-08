#!/usr/bin/env python
import networkx as nx
import numpy as np

jmp = [None] * 36
jmp[1] = 14
jmp[4] = 6
jmp[8] = 26
jmp[16] = 3
jmp[17] = 28
jmp[19] = 5
jmp[23] = 15
jmp[24] = 34
jmp[31] = 29
jmp[33] = 11

A = [[0 for x in range(36)] for y in range(36)] 
for k in range(36):
    if jmp[k] == None:
        if(k+1 == 35):
            A[k][k+1] = 1
        elif(k+1 < 36):
            A[k][k+1] = 0.5
        if(k+2 < 36):
            A[k][k+2] = 0.5
    else:
        A[k][jmp[k]] = 1

#print("Matriz de possibilidades:")
#print(A)

G = nx.from_numpy_matrix(np.matrix(A), create_using=nx.MultiDiGraph())

#print("Digrafo do Diagrama de Transições:")
#from matplotlib import pyplot
#nx.draw_networkx(G)
#pyplot.show()

def power_method(dist, interacoes, probabilidades):
    for n in range(interacoes):
        res = [0] * 36
        for i in range(36):
            for j in range(36):
                res[i] += probabilidades[j]*dist[j][i]
        probabilidades = res
    return probabilidades

inicial = [0] * 36
inicial[0] = 1
pwres = power_method(A, 100, inicial)

print("Resultado power-method:")
for x in range(36):
    print("Casa #"+str(x)+" tem possibilidade "+str(pwres[x]))


def pagerank(dist):
    alpha = 0.1
    n = 36
    res = [[0 for x in range(n)] for y in range(n)] 
    for i in range(36):
        for j in range(36):
            res[i][j] = 0.9*dist[i][j] + 0.003

    return res

inicial = [0] * 36
inicial[0] = 1
pagerank = pagerank(A)
pwrnk = power_method(pagerank, 100, inicial)

print("Resultado do power-method no pagerank:")
for x in range(36):
    print("Casa #"+str(x)+" tem possibilidade "+str(pwrnk[x]))