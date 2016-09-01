
from graph import graph

import pytest

simple_graph = graph(edges=((1,2), (2,3), (3,4), (4,1)))
two_graph = graph(edges=((1,2), (2,3),(4,5),(5,6)))

def test_findCircuit():
    circuits = list(simple_graph.findCircuit())[:-1]
    nodes = set(simple_graph.nodes)
    assert len(circuits) == 8
    for c in circuits:
        assert set(c) == nodes
        for i in range(len(c) - 1): assert c[i+1] in simple_graph.getNeighbour(c[i])
    assert len(list(two_graph.findCircuit())) == 1
