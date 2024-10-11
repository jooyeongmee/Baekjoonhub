import copy
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def bfs(y, x, visited):
    queue = deque()
    queue.append((y, x))
    while queue:
        ny, nx = queue.popleft()
        for i in range(4):
            ey = ny + dy[i]
            ex = nx + dx[i]
            if 0 <= ey < n and 0 <= ex < m:
                if graph[ey][ex] > 0 and visited[ey][ex] == 0:
                    queue.append((ey, ex))
                    visited[ey][ex] = 1
    return visited


def calculate(y, x, graph):
    temp_count = 0
    for i in range(4):
        ey = y + dy[i]
        ex = x + dx[i]
        if 0 <= ey < n and 0 <= ex < m:
            if graph[ey][ex] == 0:
                temp_count += 1

    return temp_count



year = 0
count = 0
while True:
    # 현재 빙산이 다 녹았는지 체크
    flatten_graph = sum(graph, [])
    if sum(flatten_graph) == 0:
        break

    # 현재 몇덩어리 인지 체크
    visited = [[0] * m for _ in range(n)]
    for j in range(n):
        for i in range(m):
            if graph[j][i] > 0 and visited[j][i] == 0:
                visited = bfs(j, i, visited)
                count += 1

    # 만약 두덩어리 이상이면 프린트하고 종료
    if count >= 2:
        print(year)
        exit(0)

    # 두덩어리 미만이면 일년 후의 그래프 계산
    after_graph = copy.deepcopy(graph)
    for j in range(n):
        for i in range(m):
            if graph[j][i] > 0:
                after_graph[j][i] = graph[j][i] - calculate(j, i, graph)
                if after_graph[j][i] < 0:
                    after_graph[j][i] = 0
    graph = after_graph
    year += 1
    count = 0


if count < 2:
    print(0)
