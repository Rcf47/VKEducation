import sys


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, w))

    def dijkstra(self, src, dest):
        dist = {vertex: sys.maxsize for vertex in range(1, self.V + 1)}
        dist[src] = 0
        visited = set()
        while len(visited) != self.V:
            min_vertex = None
            for vertex in range(1, self.V + 1):
                if vertex not in visited and (
                    min_vertex is None or dist[vertex] < dist[min_vertex]
                ):
                    min_vertex = vertex
            visited.add(min_vertex)
            if min_vertex == dest:
                break
            if min_vertex in self.graph:
                for neighbor, weight in self.graph[min_vertex]:
                    if dist[min_vertex] + weight < dist[neighbor]:
                        dist[neighbor] = dist[min_vertex] + weight

        return dist[dest]


N = int(input())
g = Graph(N)
for _ in range(N):
    u, v, w = map(int, input().split())
    g.add_edge(u, v, w)

start, end = map(int, input().split())


shortest_path = g.dijkstra(start, end)


print(shortest_path)
