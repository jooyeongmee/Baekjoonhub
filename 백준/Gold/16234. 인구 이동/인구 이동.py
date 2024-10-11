import copy
from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def bfs(y, x, visited):
    queue = deque([(y, x)])
    visited[y][x] = True
    result = [(y, x)]
    total = graph[y][x]
    while queue:
        ny, nx = queue.popleft()
        for i in range(4):
            ey = ny + dy[i]
            ex = nx + dx[i]
            if 0 <= ey < n and 0 <= ex < n:
                if not visited[ey][ex] and (l <= abs(graph[ny][nx] - graph[ey][ex]) <= r):
                    result.append((ey, ex))
                    total += graph[ey][ex]
                    queue.append((ey, ex))
                    visited[ey][ex] = True

    for a, b in result:
        graph[a][b] = total // len(result)
    return len(result) > 1


day = 0
while True:
    end = False
    visited = [[False] * n for _ in range(n)]

    # 하루동안 일어날 수 있는 인구이동
    for j in range(n):
        for i in range(n):
            if not visited[j][i]:
                if bfs(j, i, visited):
                    end = True

    # 인구이동이 한번도 일어나지 않았으면 day 프린트하고 종료
    if end:
        day += 1
    else:
        print(day)
        exit(0)



