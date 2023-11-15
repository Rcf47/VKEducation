from collections import defaultdict


def count_social_circles(edges):
    graph = defaultdict(list)
    visited = set()

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    count = 0
    for node in graph:
        if node not in visited:
            dfs(node)
            count += 1

    return count


n = int(input())
edges = []
for _ in range(n):
    u, v = map(int, input().split())
    edges.append((u, v))

result = count_social_circles(edges)

print(result)
