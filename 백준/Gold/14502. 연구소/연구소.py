from itertools import combinations
from collections import deque
import copy
import sys
input = sys.stdin.readline

## 조합: nCk = (n! / (k! * (n-k)!))
## nC3 = (n! / (3! * (n-3)!)) = (n*(n-1)*(n-2)) / 6

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def get_walls():
    empty = []
    for j in range(n):
        for i in range(m):
            if graph[j][i] == 0:
                empty.append((j, i))
    return empty

def bfs(y, x, temp_graph, check):
    q = deque()
    q.append((y, x))
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if temp_graph[ny][nx] == 0 and not check[ny][nx]:
                    check[ny][nx] = True
                    temp_graph[ny][nx] = 2
                    q.append((ny, nx))
    return temp_graph, check

result = 0
for combo in list(combinations(get_walls(), 3)):
    temp_graph = copy.deepcopy(graph)
    check = [[False] * m for _ in range(n)]

    for (y, x) in combo:
        temp_graph[y][x] = 1
    
    for j in range(n):
        for i in range(m):
            if temp_graph[j][i] == 2 and not check[j][i]:
                check[j][i] = True
                temp_graph, check = bfs(j, i, temp_graph, check)
    
    count = 0
    for j in range(n):
        for i in range(m):
            if temp_graph[j][i] == 0:
                count += 1
    
    result = max(result, count)

print(result)
    
    

