from collections import deque
import sys

input = sys.stdin.readline

n = int(input().rstrip())

data = [list(map(int, input().rstrip())) for _ in range(n)]
check = [[False] * n for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

answer = []

def bfs(y, x):
    rs = 1
    queue = deque()
    queue.append((y, x))
    while queue:
        ey, ex = queue.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < n:
                if data[ny][nx] == 1 and check[ny][nx] == False:
                    rs += 1
                    check[ny][nx] = True
                    queue.append((ny, nx))

    return rs


for j in range(n):
    for i in range(n):
        if data[j][i] == 1 and check[j][i] == False:
            check[j][i] = True
            answer.append(bfs(j, i))

print(len(answer))
answer.sort()
for i in range(len(answer)):
    print(answer[i])
