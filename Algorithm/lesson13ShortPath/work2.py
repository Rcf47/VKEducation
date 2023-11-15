import heapq


def dijkstra(graph, start, end):
    # Инициализация расстояний
    dist = {vertex: float("infinity") for vertex in graph}
    dist[start] = 0

    # Инициализация приоритетной очереди с начальной вершиной
    priority_queue = [(0, start)]

    while priority_queue:
        current_dist, current_vertex = heapq.heappop(priority_queue)

        # Пропускаем вершины, которые мы уже рассмотрели
        if current_dist > dist[current_vertex]:
            continue

        # Обновляем расстояния до соседей
        for neighbor, weight in graph[current_vertex]:
            if dist[current_vertex] + weight < dist[neighbor]:
                dist[neighbor] = dist[current_vertex] + weight
                heapq.heappush(priority_queue, (dist[neighbor], neighbor))

    return dist[end]


n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n)]
start, end = map(int, input().split())


graph = {i: [] for i in range(1, n + 1)}
for edge in edges:
    graph[edge[0]].append((edge[1], 1))  # Предполагаем, что вес каждого ребра равен 1


result = dijkstra(graph, start, end)


print(result)
