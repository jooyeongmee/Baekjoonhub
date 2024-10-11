from collections import deque
import copy
import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]
robot = []

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def calculate(y, x, new_graph):
    count = 0
    amount = graph[y][x] // 5
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < r and 0 <= nx < c and new_graph[ny][nx] != -1:
            new_graph[ny][nx] += amount
            count += 1
    new_graph[y][x] -= amount * count
    return new_graph


def rotate_up(new_graph):
    y, x = robot[0], 1
    move = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    direction = 0
    temp = 0
    while True:
        if x == c - 1:
            direction = 1
        if y == 0:
            direction = 2
        if x == 0:
            direction = 3
        if x == 0 and y == robot[0]:
            break
        new_graph[y][x], temp = temp, new_graph[y][x]
        y = y + move[direction][0]
        x = x + move[direction][1]
    return new_graph


def rotate_down(new_graph):
    y, x = robot[1], 1
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    direction = 0
    temp = 0
    while True:
        if x == c - 1:
            direction = 1
        if y == r - 1:
            direction = 2
        if x == 0:
            direction = 3
        if x == 0 and y == robot[1]:
            break
        new_graph[y][x], temp = temp, new_graph[y][x]
        y = y + move[direction][0]
        x = x + move[direction][1]
    return new_graph


for _ in range(t):
    # 1초동안 발생하는 미세먼지 확산
    new_graph = copy.deepcopy(graph)
    for j in range(r):
        for i in range(c):
            if graph[j][i] > 0:
                new_graph = calculate(j, i, new_graph)
            if graph[j][i] == -1:
                robot.append(j)

    # 공기청소기 rotate

    # 위의 그래프를 반시계 방향으로 회전
    new_graph = rotate_up(new_graph)

    # 아래 그래프를 반시계 방향으로 회전
    new_graph = rotate_down(new_graph)

    graph = new_graph


print(sum(sum(graph, [])) + 2)




