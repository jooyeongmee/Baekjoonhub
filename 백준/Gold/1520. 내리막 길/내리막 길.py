import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]

dp = [[-1] * n for _ in range(m)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(y, x):
    if y == m - 1 and x == n - 1:
        return 1
    
    if dp[y][x] != -1:
        return dp[y][x]
    
    dp[y][x] = 0
    
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < m and  0 <= nx < n:
            if graph[ny][nx] < graph[y][x]:
                dp[y][x] += dfs(ny, nx)

    return dp[y][x]

print(dfs(0, 0))


