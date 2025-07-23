import heapq
import sys
sys.setrecursionlimit(10**6)

v, e = map(int, input().split())
queue = []
for _ in range(e):
    a, b, c = map(int, input().split())
    heapq.heappush(queue, (c, a, b))

parents = [i for i in range(v + 1)]

def find_parent(x):
    if parents[x] == x: # 자신이 곧 대표 노드인 경우
        return x
    # 대표 노드를 찾으면서 경로상의 모든 노드의 부모를 대표 노드로 직접 연결 (경로 압축)
    parents[x] = find_parent(parents[x])
    return parents[x]

def union_parent(x, y):
    root_x = find_parent(x)
    root_y = find_parent(y)
    if root_x != root_y:
        parents[root_y] = root_x
        return True
    return False # 이미 같은 집합에 속해 있음 (사이클 발생)
        
result = 0
edges_count = 0
while queue:
    distance, node1, node2 = heapq.heappop(queue)
     # 이 간선을 추가했을 때 사이클이 형성되지 않는다면
    if union_parent(node1, node2):
        result += distance 
        edges_count += 1
        
        if edges_count == v - 1:
            break

print(result)