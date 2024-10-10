from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
result = []

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def bfs(y, x, map_info):
    queue = deque()
    queue.append((y, x))
    while queue:
        ny, nx = queue.popleft()
        for i in range(4):
            ey = ny + dy[i]
            ex = nx + dx[i]
            if 0 <= ey < n and 0 <= ex < n:
                if visited[ey][ex] == False and map_info[ey][ex] == 0:
                    queue.append((ey, ex))
                    visited[ey][ex] = True



max_value = max(sum(graph, []))

for h in range(0, max_value+1):
    count = 0
    map_info = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    for j in range(n):
        for i in range(n):
            if graph[j][i] <= h:
                map_info[j][i] = 1

    for j in range(n):
        for i in range(n):
            if map_info[j][i] == 0 and visited[j][i] == False:
                bfs(j, i, map_info)
                count += 1
    result.append(count)

print(max(result))
