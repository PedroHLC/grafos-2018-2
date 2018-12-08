#!/usr/bin/env python
import networkx as nx
import numpy as np

Homens = {
    'abe': [ 'abi', 'eve', 'cath', 'ivy', 'jan', 'dee', 'fay', 'bea', 'hope', 'gay' ],
    'bob': [ 'cath', 'hope', 'abi', 'dee', 'eve', 'fay', 'bea', 'jan', 'ivy', 'gay' ],
    'col': [ 'hope', 'eve', 'abi', 'dee', 'bea', 'fay', 'ivy', 'gay', 'cath', 'jan' ],
    'dan': [ 'ivy', 'fay', 'dee', 'gay', 'hope', 'eve', 'jan', 'bea', 'cath', 'abi' ],
    'ed' : [ 'jan', 'dee', 'bea', 'cath', 'fay', 'eve', 'abi', 'ivy', 'hope', 'gay' ],
    'fred':[ 'bea', 'abi', 'dee', 'gay', 'eve', 'ivy', 'cath', 'jan', 'hope', 'fay' ],
    'gav': [ 'gay', 'eve', 'ivy', 'bea', 'cath', 'abi', 'dee', 'hope', 'jan', 'fay' ],
    'hal': [ 'abi', 'eve', 'hope', 'fay', 'ivy', 'cath', 'jan', 'bea', 'gay', 'dee' ],
    'ian': [ 'hope', 'cath', 'dee', 'gay', 'bea', 'abi', 'fay', 'ivy', 'jan', 'eve' ],
    'jon': [ 'abi', 'fay', 'jan', 'gay', 'eve', 'bea', 'dee', 'cath', 'ivy', 'hope' ]
}

Mulheres = {
    'abi': [ 'bob', 'fred', 'jon', 'gav', 'ian', 'abe', 'dan', 'ed', 'col', 'hal' ],
    'bea': [ 'bob', 'abe', 'col', 'fred', 'gav', 'dan', 'ian', 'ed', 'jon', 'hal' ],
    'cath': [ 'fred', 'bob', 'ed', 'gav', 'hal', 'col', 'ian', 'abe', 'dan', 'jon' ],
    'dee': [ 'fred', 'jon', 'col', 'abe', 'ian', 'hal', 'gav', 'dan', 'bob', 'ed' ],
    'eve': [ 'jon', 'hal', 'fred', 'dan', 'abe', 'gav', 'col', 'ed', 'ian', 'bob' ],
    'fay': [ 'bob', 'abe', 'ed', 'ian', 'jon', 'dan', 'fred', 'gav', 'col', 'hal' ],
    'gay': [ 'jon', 'gav', 'hal', 'fred', 'bob', 'abe', 'col', 'ed', 'dan', 'ian' ],
    'hope': [ 'gav', 'jon', 'bob', 'abe', 'ian', 'dan', 'hal', 'ed', 'col', 'fred' ],
    'ivy': [ 'ian', 'col', 'hal', 'gav', 'fred', 'bob', 'abe', 'ed', 'jon', 'dan' ],
    'jan': [ 'ed', 'hal', 'gav', 'abe', 'bob', 'jon', 'col', 'ian', 'fred', 'dan' ]
}

Casais = {}
Sozinhas = list(Mulheres.keys())
Sozinhos = list(Homens.keys())
Propostas = {
    'abi': 0,
    'bea': 0,
    'cath': 0,
    'dee': 0,
    'eve': 0,
    'fay': 0,
    'gay': 0,
    'hope': 0,
    'ivy': 0,
    'jan': 0
}

def such_a_woman():
    for x in Sozinhas:
        if(Propostas[x] < len(Homens.keys())):
            return x
    return None;

while True:
    m = such_a_woman();
    if(m == None):
        break;
    h = Mulheres[m][Propostas[m]]
    if h in Sozinhos:
        Casais[h] = m
        Sozinhos.remove(h)
        Sozinhas.remove(m)
    else:
        if Homens[h].index(Casais[h]) < Homens[h].index(m):
            Sozinhas.append(Casais[h])
            Casais[h] = m
            Sozinhas.remove(m)
    Propostas[m] += 1

print(Casais)