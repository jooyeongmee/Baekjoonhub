import sys
input = sys.stdin.readline

r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]
visited_alphabets = [False] * 26

max_count = 0
count = 0
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(y, x):
    global max_count, count, visited_alphabets
    count += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if  0<= ny < r and 0<= nx < c:
            if visited_alphabets[ord(graph[ny][nx]) - ord('A')] == False:
                visited_alphabets[ord(graph[ny][nx]) - ord('A')] = True
                dfs(ny, nx)
    max_count = max(max_count, count)
    visited_alphabets[ord(graph[y][x]) - ord('A')] = False
    count -= 1  

visited_alphabets[ord(graph[0][0]) - ord('A')] = True
dfs(0, 0)
print(max_count)

