from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input().strip()) for _ in range(n)]
check = [[False] * n for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x, color):
    q = deque()
    q.append((y, x))
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < n:
                if color == 'RG':
                    if (graph[ny][nx] == 'R' or graph[ny][nx] == 'G') and not check[ny][nx]:
                        check[ny][nx] = True
                        q.append((ny, nx))
                else:
                    if graph[ny][nx] == color and not check[ny][nx]:
                        check[ny][nx] = True
                        q.append((ny, nx))
                    
    
    
had_green_count = 0
for j in range(n):
    for i in range(n):
        if graph[j][i] == 'R' and not check[j][i]:
            had_green_count += 1 
            check[j][i] = True
            bfs(j, i, 'R')
        
        if graph[j][i] == 'B' and not check[j][i]:
            had_green_count += 1 
            check[j][i] = True
            bfs(j, i, 'B')
        
        if graph[j][i] == 'G' and not check[j][i]:
            had_green_count += 1 
            check[j][i] = True
            bfs(j, i, 'G')

check = [[False] * n for _ in range(n)]
count = 0
for j in range(n):
    for i in range(n):
        if (graph[j][i] == 'R' or graph[j][i] == 'G') and not check[j][i]:
            count += 1 
            check[j][i] = True
            bfs(j, i, 'RG')
        
        if graph[j][i] == 'B' and not check[j][i]:
            count += 1 
            check[j][i] = True
            bfs(j, i, 'B')

print(had_green_count, count)