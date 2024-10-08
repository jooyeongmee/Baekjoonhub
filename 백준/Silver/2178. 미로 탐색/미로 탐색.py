from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    while queue:
        ey, ex = queue.popleft()
        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 1:
                graph[ny][nx] = graph[ey][ex] + 1
                queue.append((ny, nx))


bfs(0, 0)
print(graph[n-1][m-1])

