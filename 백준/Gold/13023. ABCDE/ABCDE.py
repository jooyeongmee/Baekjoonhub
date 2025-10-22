import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

check = [False] * n
max_distance = 0
count = 0

def dfs(node):
    global count, max_distance
    check[node] = True
    count += 1
    for next_node in graph[node]:
        if not check[next_node]:
            dfs(next_node)
    
    max_distance = max(max_distance, count)
    if (max_distance >= 5):
        print(1)
        exit()
    count -= 1
    check[node] = False

for i in range(n):    
    dfs(i)
print(0)