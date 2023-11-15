def dfs(v, p, timer, tin, low, visited, adjList, bridges):
    visited[v] = True
    tin[v] = low[v] = timer
    timer += 1
    for to in adjList[v]:
        if to == p:
            continue
        if visited[to]:
            low[v] = min(low[v], tin[to])
        else:
            dfs(to, v, timer, tin, low, visited, adjList, bridges)
            low[v] = min(low[v], low[to])
            if low[to] > tin[v]:
                bridges.append((v, to))


def findBridges(adjList):
    n = len(adjList)
    tin = [-1] * n
    low = [-1] * n
    visited = [False] * n
    bridges = []
    timer = 0
    for i in range(n):
        if not visited[i]:
            dfs(i, -1, timer, tin, low, visited, adjList, bridges)
    return bridges


n, m = map(int, input().split())
adjList = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adjList[u].append(v)
    adjList[v].append(u)

bridges = findBridges(adjList)
for bridge in bridges:
    print(f"Мост: {bridge[0]} - {bridge[1]}")
