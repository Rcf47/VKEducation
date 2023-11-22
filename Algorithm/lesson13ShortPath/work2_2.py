def find_min_transfers(edges, start, end):
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    queue = [(start, 0)]
    while queue:
        station, transfers = queue.pop(0)
        visited.add(station)
        if station == end:
            return transfers
        for neighbor in graph[station]:
            if neighbor not in visited:
                queue.append((neighbor, transfers + 1))

    return "No path found"


N = int(input())
edges = []
for _ in range(N):
    u, v = map(int, input().split())
    edges.append((u, v))

start, end = map(int, input().split())

result = find_min_transfers(edges, start, end)
if type(result) == int:
    result = result - 1
print(result)
