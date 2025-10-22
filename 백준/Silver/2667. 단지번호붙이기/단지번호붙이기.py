import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
check = [[False] * n for _ in range(n)]

each = 0
result = []

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(y, x):
    global each
    each += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < n and 0 <= nx < n:
            if graph[ny][nx] == 1 and not check[ny][nx]:
                check[ny][nx] = True
                dfs(ny, nx)
                
                
for j in range(n):
    for i in range(n):
        if graph[j][i] == 1 and not check[j][i]:
            check[j][i] = True
            each = 0
            dfs(j, i)
            result.append(each)

result.sort()
print(len(result))

for r in result:
    print(r)