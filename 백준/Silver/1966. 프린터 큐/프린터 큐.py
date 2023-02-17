import sys
import heapq

def make_heap(list):
  heap = []
  for l in list:
    heapq.heappush(heap, -l)
  return heap
  
num = int(input())

for i in range(num):
  N, target_idx = map(int, sys.stdin.readline().split())
  queue = list(map(int, sys.stdin.readline().split()))

  target = queue[target_idx]
  heap = make_heap(queue)
  
  queue[target_idx] = 0

  j = 0
  count = 0
  while True:
    
    if j == len(queue): j = 0

    most_import = -heap[0]
    
    if (queue[j] == 0 and target == most_import) or len(queue) == 1:
        count += 1
        print(count)
        break
      
    if queue[j] != most_import:
      j += 1
    else:
      count += 1
      top = queue[j]
      del queue[j]
      heapq.heappop(heap)
      
