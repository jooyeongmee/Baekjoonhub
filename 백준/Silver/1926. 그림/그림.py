import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
check = [[False] * m for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x):
    q = deque()
    q.append((y, x))
    size = 1
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if  0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 1 and not check[ny][nx]:
                    check[ny][nx] = True
                    q.append((ny, nx))
                    size += 1
    return size

max_value = 0
count = 0
for j in range(n):
    for i in range(m):
        if graph[j][i] == 1 and not check[j][i]:
            check[j][i] = True
            max_value = max(max_value, bfs(j, i))
            count += 1
            
print(count)
print(max_value)