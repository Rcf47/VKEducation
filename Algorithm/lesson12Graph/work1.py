def find_triangles():
    n = int(input())
    edges = []
    for _ in range(n):
        u, v = map(int, input().split())
        edges.append((u, v))
    graph = {}
    for i in range(1, n + 1):
        graph[i] = set()
    for edge in edges:
        u, v = edge
        graph[u].add(v)
        graph[v].add(u)
    for u in range(1, n + 1):
        for v in range(u + 1, n + 1):
            if v in graph[u]:
                for w in range(v + 1, n + 1):
                    if w in graph[u] and w in graph[v]:
                        return "YES"
    return "NO"


result = find_triangles()
print(result)
