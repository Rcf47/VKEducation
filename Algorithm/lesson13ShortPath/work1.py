import heapq


def dijkstra(graph, start, end):
    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    shortest_path = []
    current_vertex = end

    while current_vertex != start:
        shortest_path.append(current_vertex)
        current_vertex = graph[current_vertex][1]

    shortest_path.append(start)
    shortest_path.reverse()

    return shortest_path, distances[end]


n = int(input())
graph = {}

for _ in range(n):
    u, v, weight = map(int, input().split())

    if u not in graph:
        graph[u] = {}

    if v not in graph:
        graph[v] = {}

    graph[u][v] = weight
    graph[v][u] = weight

start, end = map(int, input().split())


shortest_path, duration = dijkstra(graph, start, end)
print(len(shortest_path))
print(*shortest_path)
print(duration)
