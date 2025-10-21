from collections import deque
import sys
input = sys.stdin.readline

length = 100001
n, k = map(int, input().split())
visited = [-1] * length

visited[n] = 0
q = deque()
q.append(n)

dx = [0, -1, 1]
def bfs():
    while q:
        current = q.popleft()
        time = visited[current]
        if current == k:
            print(time)
            return
        
        for i in range(3):
            nx = 2 * current if i == 0 else current + dx[i]
            
            if  0 <= nx < length and visited[nx] == -1:
                visited[nx] = time if i == 0 else time + 1
                q.append(nx)
    

bfs()
 