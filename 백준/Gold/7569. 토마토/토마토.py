from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())
visited = [[[0] * m for _ in range(n)] for _ in range(h)]
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]


# 오 앞 왼 뒤 위 아래
dz = [0, 0, 0, 0, 1, -1]
dy = [0, 1, 0, -1, 0, 0]
dx = [1, 0, -1, 0, 0, 0]

queue = deque()


def bfs():
    while queue:
        nz, ny, nx = queue.popleft()
        for i in range(6):
            ez = nz + dz[i]
            ey = ny + dy[i]
            ex = nx + dx[i]
            if 0<=ez<h and 0<=ey<n and 0<=ex<m:
                if graph[ez][ey][ex] == 0 and visited[ez][ey][ex] == 0:
                    graph[ez][ey][ex] = graph[nz][ny][nx] + 1
                    queue.append((ez, ey, ex))
                    visited[ez][ey][ex] = 1


for k in range(h):
    for j in range(n):
        for i in range(m):
            if graph[k][j][i] == 1 and visited[k][j][i] == 0:
                queue.append((k, j, i))
                visited[k][j][i] = 1

bfs()


flag = False
day = 0
for k in range(h):
    for j in range(n):
        for i in range(m):
            if graph[k][j][i] == 0:
                flag = True
            day = max(day, graph[k][j][i])

if flag:
    print(-1)
else:
    print(day - 1)

