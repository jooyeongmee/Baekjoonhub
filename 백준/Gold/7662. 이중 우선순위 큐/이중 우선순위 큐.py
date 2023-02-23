import sys
import heapq

#테스트케이스 개수
T = int(input())

for i in range(T):
  dict = {}
  cmd = []
  Q_max = [] #max 값을 하나씩 지움
  Q_min = [] #min 값을 하나씩 지움
  
  k =  int(sys.stdin.readline()) #Q에 적용할 연산의 개수
  
  for _ in range(k):
    op, n = sys.stdin.readline().split() #연산을 나타내는 문자(‘D’ 또는 ‘I’)와 정수 n
    n = int(n)
    cmd.append([op, n])

  for j in range(k):
    op = cmd[j][0]
    n = cmd[j][1]
    # print(j, op, n, dict)
    if op == 'I':
      heapq.heappush(Q_max, -n)
      heapq.heappush(Q_min, n)
      if n in dict:
        dict[n] += 1
      else :
        dict[n] = 1
        
    elif len(dict):
      if n == 1:
        while True:
          top = heapq.heappop(Q_max)
          if -top in dict.keys():
            dict[-top] -= 1
            if dict[-top] <= 0:
              del dict[-top]
            break
            
 
      if n == -1:
        while True:
          top = heapq.heappop(Q_min)
          if top in dict.keys():
            dict[top] -= 1
            if dict[top] <= 0:
              del dict[top]
            break
  # print(dict)
  # print(Q_max)
  # print(Q_min)
  for _ in range(len(Q_min)):
    if Q_min[0] in dict.keys(): break
    heapq.heappop(Q_min)
    
  for _ in range(len(Q_max)):
    if -Q_max[0] in dict.keys(): break
    heapq.heappop(Q_max)  
    
  if len(dict):
    print(-Q_max[0], Q_min[0])
  else:
    print("EMPTY")


      
      
    
    