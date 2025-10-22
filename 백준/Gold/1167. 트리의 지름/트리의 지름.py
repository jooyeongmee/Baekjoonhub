import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

v = int(input())
graph = [[] for _ in range(v+1)]
visited = [False] * (v + 1)

for _ in range(v):
    data = list(map(int, input().split()))
    node = data[0]
    for i in range(1, len(data)-1, 2):
        if data[i] == -1:
            break
        graph[node].append((data[i], data[i+1]))


target_node = [0, 0]

def dfs(node, current_distance):
    global target_node, visited
    visited[node] = True
    
    if current_distance > target_node[1]:
        target_node = [node, current_distance]
        
    for next_node, distance in graph[node]:
        if not visited[next_node]:
            dfs(next_node, current_distance + distance)
       

dfs(1, 0)
farthest_node = target_node[0]

visited = [False] * (v + 1)
target_node = [0, 0]

dfs(farthest_node, 0)

print(target_node[1])
