import heapq

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

costs = [float('inf')] * (n + 1)
costs[start] = 0

queue = [(0, start)]  

while queue:
    cost, now = heapq.heappop(queue)
    
    if costs[now] < cost:
        continue
    
    for next_node, next_cost in graph[now]:
        new_cost = cost + next_cost
        
        if new_cost < costs[next_node]:
            costs[next_node] = new_cost
            heapq.heappush(queue, (new_cost, next_node))           
print(costs[end])
    
    
 