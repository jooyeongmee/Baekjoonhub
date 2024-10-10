from collections import deque
import sys
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
visited = [False] * (f+1)
flag = False


def bfs():
    global flag
    queue = deque()
    queue.append((s, 0))

    while queue:
        position, count = queue.popleft()
        if position == g:
            flag = True
            return count
        up = position + u
        down = position - d
        if 1 <= up <= f and visited[up] == False:
            queue.append((up, count+1))
            visited[up] = True
        if 1 <= down <= f and visited[down] == False:
            queue.append((down, count+1))
            visited[down] = True


result = bfs()
if flag:
    print(result)
else:
    print("use the stairs")
