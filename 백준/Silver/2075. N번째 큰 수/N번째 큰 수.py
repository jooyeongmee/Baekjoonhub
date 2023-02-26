import sys
import heapq

N = int(input())

def get_input(N):
  data = []
  heap = []
  for _ in range(N):
    input_data = list(map(int, sys.stdin.readline().strip().split()))
    for num in input_data:
      heapq.heappush(heap, -num)
    if len(heap) > N:
      data = []
      for _ in range(N):
        data.append(-heapq.heappop(heap))
      heap = [-_ for _ in data]
      heapq.heapify(heap)
    
  if N == 1:
    print(-heap[0])
  else:
    print(data[N-1])
  
get_input(N)