import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

k = int(input())

def solve():
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    
    for _ in range(e):
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)
        
    check = [0] * (v + 1)
    is_bipartite = True
    
    def dfs(node, tag):
        nonlocal is_bipartite
        if check[node] == 0:
            check[node] = tag
        elif check[node] != tag:
            is_bipartite = False
            return
        for next_node in graph[node]:
            if check[next_node] != -tag:
                dfs(next_node, -tag)
        
    
    for i in range(1, v+1):
        if check[i] == 0:
            dfs(i, 1)
           

    if is_bipartite:
        print("YES")
    else:
        print("NO")
        
         
for _ in range(k):
    solve()