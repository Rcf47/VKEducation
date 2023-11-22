def find_min_transfers(N, edges, start, end):
    graph = {}
    for i in range(N):
        u, v = edges[i]
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    queue = [(start, 0)]
    while queue:
        node, transfers = queue.pop(0)
        if node == end:
            return transfers
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, transfers + 1))
                visited.add(
                    neighbor
                )  # Добавляем соседа в посещенные, чтобы избежать повторного посещения
    return "No path found"


N = 4
edges = [(1, 2), (2, 3), (3, 4), (4, 5)]
start = 1
end = 5

result = find_min_transfers(N, edges, start, end)
print(result)
