import sys
input = sys.stdin.readline

r, c = map(int, input().split())
graph = [list(map(lambda x: ord(x) - ord('A'), input().strip())) for _ in range(r)]
visited_alphabets = [False] * 26

max_count = 0
count = 0
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(y, x):
    global max_count, count
    count += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if  0<= ny < r and 0<= nx < c:
            if visited_alphabets[graph[ny][nx]] == False:
                visited_alphabets[graph[ny][nx]] = True
                dfs(ny, nx)
    max_count = max(max_count, count)
    visited_alphabets[graph[y][x]] = False
    count -= 1  

visited_alphabets[graph[0][0]] = True
dfs(0, 0)
print(max_count)

