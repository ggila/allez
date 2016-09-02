
from graph import graph

import pytest

simple_graph = graph(edges=((1,2), (2,3), (3,4), (4,1)))
two_graph = graph(edges=((1,2), (2,3),(4,5),(5,6)))
simple_directed_graph = graph(edges=((1,2,True), (2,3,True), (3,4,True), (4,1,True)))

def test_findCircuit_simple():
    circuits = list(simple_graph.findCircuit())[:-1]
    nodes = set(simple_graph.nodes)
    assert len(circuits) == 8
    for c in circuits:
        assert set(c) == nodes
        for i in range(len(c) - 1): assert c[i+1] in simple_graph.getNeighbour(c[i])

def test_findCircuit_two():
    assert len(list(two_graph.findCircuit())) == 1

def test_findCircuit_simpledirected():
    circuits = list(simple_directed_graph.findCircuit())[:-1]
    nodes = set(simple_directed_graph.nodes)
    assert len(circuits) == 4
    for c in circuits:
        assert set(c) == nodes
        for i in range(len(c) - 1): assert c[i+1] in simple_directed_graph.getNeighbour(c[i])
