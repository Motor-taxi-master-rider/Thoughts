import sys
import numpy as np
sys.path.append('../')
from data_structure.Graph import Graph


def topsort(graph: Graph):
    def helper(graph: Graph, index: int):
        graph.set_mark(index, Graph.VISITED)

        col = graph.first(index)
        while col < graph.n():
            if graph.get_mark(col) == Graph.UNVISITED:
                helper(graph, col)
            col = graph.next(index, col)
        print(index + 1)

    for i in range(graph.n()):
        graph.set_mark(i, Graph.UNVISITED)

    for i in range(graph.n()):
        if graph.get_mark(i) == Graph.UNVISITED:
            helper(graph, i)


if __name__ == '__main__':
    graph = Graph(7)
    graph._matrix = np.array([[0, 1, 1, np.inf, np.inf, np.inf, np.inf],
                              [np.inf, 0, np.inf, 1, np.inf, 1, np.inf],
                              [np.inf, np.inf, 0, 1, np.inf, np.inf, np.inf],
                              [np.inf, np.inf, np.inf, 0, 1, np.inf, np.inf],
                              [np.inf, np.inf, np.inf, np.inf, 0, np.inf, 1],
                              [np.inf, np.inf, np.inf, np.inf, np.inf, 0, np.inf],
                              [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 0]])

    topsort(graph)
