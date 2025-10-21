from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = list(list(map(int, input().strip())) for _ in range(n))
visited = [[[0] * 2 for _ in range(m)]  for _ in range(n)]

q = deque()
q.append((0, 0, 0))
visited[0][0][0] = 1

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs():
    if (n == m == 1):
        print(1)
        return
    
    while q:
        ey, ex, wall = q.popleft()
        current_step = visited[ey][ex][wall]
        
        if (ey == n-1 and ex == m-1):
            print(current_step)
            return
        
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 0:
                    if visited[ny][nx][wall] == 0:
                        visited[ny][nx][wall] = current_step + 1
                        q.append((ny, nx, wall))
                elif graph[ny][nx] == 1:
                    if wall == 0:
                        new_wall = 1
                        if visited[ny][nx][new_wall] == 0:
                            visited[ny][nx][new_wall] = current_step + 1
                            q.append((ny, nx, new_wall))
    print(-1)
                        

bfs()
    
