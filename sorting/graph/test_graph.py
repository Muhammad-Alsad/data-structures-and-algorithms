import pytest 
from collections import deque
from graph import Graph

def test_get_vertices():
    graph = Graph()
    v1 = graph.add_vertix("A")
    v2 = graph.add_vertix("B")
    vertices = graph.get_vertices()
    assert len(vertices) == 2
    assert v1 in vertices
    assert v2 in vertices

def test_add_multiple_edges():
    graph = Graph()
    v1 = graph.add_vertix("A")
    v2 = graph.add_vertix("B")
    v3 = graph.add_vertix("C")
    graph.add_edge(v1, v2, 5)
    graph.add_edge(v1, v3, 7)
    graph.add_edge(v2, v3, 3)
    neighbors = graph.get_neighbors(v1)
    assert len(neighbors) == 2
    assert neighbors[0].vertix == v2
    assert neighbors[0].weight == 5
    assert neighbors[1].vertix == v3
    assert neighbors[1].weight == 7

def test_get_nonexistent_vertex_neighbors():
    graph = Graph()
    v1 = graph.add_vertix("A")
    v2 = graph.add_vertix("B")
    neighbors = graph.get_neighbors(v2)  
    assert len(neighbors) == 0


def test_size():
    graph = Graph()
    v1 = graph.add_vertix("A")
    v2 = graph.add_vertix("B")
    v3 = graph.add_vertix("C")
    v4 = graph.add_vertix("D")
    assert graph.size() == 4
    v5 = graph.add_vertix("F")
    assert graph.size() == 5    





