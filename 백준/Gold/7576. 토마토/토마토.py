from collections import deque

import sys
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
q = deque()

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs():
    while q:
        ey, ex = q.popleft()
        current_day = graph[ey][ex]
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = current_day + 1
                    q.append((ny, nx))
                    

for j in range(n):
    for i in range(m):
        if graph[j][i] == 1:
            q.append((j, i))

bfs()


day = 0
for j in range(n):
    for i in range(m):
        if (graph[j][i] == 0):
            print(-1)
            exit()
        else:
            day = max(day, graph[j][i])
            
print(day - 1)
            
            