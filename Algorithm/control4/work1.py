from typing import List, Tuple


class Edge:
    def __init__(self, source: int, destination: int, weight: int):
        self.source = source
        self.destination = destination
        self.weight = weight


def bellman_ford(edges: List[Edge], num_vertices: int, source: int) -> None:
    distance = [float("inf")] * num_vertices
    distance[source] = 0

    for _ in range(num_vertices - 1):
        for edge in edges:
            if (
                distance[edge.source] != float("inf")
                and distance[edge.source] + edge.weight < distance[edge.destination]
            ):
                distance[edge.destination] = distance[edge.source] + edge.weight

    for edge in edges:
        if (
            distance[edge.source] != float("inf")
            and distance[edge.source] + edge.weight < distance[edge.destination]
        ):
            print("Graph contains negative cycle")

    for i in range(num_vertices):
        print(f"Shortest path from {source} to {i}: {distance[i]}")


if __name__ == "__main__":
    edges = [
        Edge(1, 2, 1),
        Edge(1, 3, 4),
        Edge(2, 3, -3),
        Edge(3, 4, 2),
        Edge(4, 2, -1),
    ]

    num_vertices = 5
    source = 1

    bellman_ford(edges, num_vertices, source)
