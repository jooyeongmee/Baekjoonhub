import sys
input = sys.stdin.readline

n = int(input())
person1, person2 = map(int, input().split())
m = int(input())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

count = 0
flag = False


def dfs(v, s):
    global count, flag
    visited[v] = True
    if v == s:
        flag = True
        print(count)
    for i in range(1, n+1):
        if graph[v][i] == 1 and visited[i] == False:
            count += 1
            dfs(i, s)
    count -= 1


dfs(person1, person2)
if not flag:
    print(-1)



