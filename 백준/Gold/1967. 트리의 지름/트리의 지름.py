import sys

sys.setrecursionlimit(10 ** 9)


def dfs(graph, v, visited, weight):
    visited[v] = weight

    for (i, w) in graph[v]:
        if visited[i] == -1:
            dfs(graph, i, visited, weight + w)


n = int(input())

graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

visited = [-1] * (n + 1)
dfs(graph, 1, visited, 0)

max_idx = visited.index(max(visited))

visited = [-1] * (n + 1)
dfs(graph, max_idx, visited, 0)

print(max(visited))