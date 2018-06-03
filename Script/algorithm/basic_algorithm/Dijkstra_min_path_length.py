import numpy as np
import itertools

from data_structure.Graph import Graph


def Dijkstra(graph: Graph, start_index: int) -> np.array:
    """
    Compute shortest path distances from `start_index`.
    Return a distance list which each index stand for distance from the starting point.
    """

    def min_vertex() -> int:
        """ Return min value vertex index in the distance list."""
        nonlocal graph, distance
        vertex_index = next(v for v in range(graph.n()) if graph.get_mark(v) == Graph.UNVISITED)
        for v in range(graph.n()):
            if graph.get_mark(v) == Graph.UNVISITED and distance[v] < distance[vertex_index]:
                vertex_index = v
        return vertex_index

    distance = graph._matrix[start_index]
    graph.set_mark(start_index, Graph.VISITED)

    for _ in itertools.repeat(None, graph.n() - 1):
        index = min_vertex()
        if distance[index] == np.Inf:
            return distance
        graph.set_mark(index, Graph.VISITED)

        col = graph.first(index)
        while col < graph.n():
            curve_distance = distance[index] + graph.weight(index, col)
            if distance[col] > curve_distance:
                distance[col] = curve_distance
            col = graph.next(index, col)

    return distance


if __name__ == '__main__':
    graph = Graph(5)
    graph._matrix = np.array([[0, 10, 3, 20, np.inf],
                              [np.inf, 0, np.inf, 5, np.inf],
                              [np.inf, 2, 0, np.inf, 15],
                              [np.inf, np.inf, np.inf, 0, 11],
                              [np.inf, np.inf, np.inf, np.inf, 0]])

    assert graph.first(2) == 1
    assert graph.next(2, 1) == 4
    assert list(Dijkstra(graph, 0)) == [0, 5, 3, 10, 18]

    graph.reset_mark()
    assert list(Dijkstra(graph, 1)) == [np.inf, 0, np.inf, 5, 16]

    graph.reset_mark()
    assert list(Dijkstra(graph, 2)) == [np.inf, 2, 0, 7, 15]

    graph.reset_mark()
    assert list(Dijkstra(graph, 3)) == [np.inf, np.inf, np.inf, 0, 11]

    graph.reset_mark()
    assert list(Dijkstra(graph, 4)) == [np.inf, np.inf, np.inf, np.inf, 0]
