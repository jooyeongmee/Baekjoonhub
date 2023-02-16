import sys

N = int(input())
queue = []
for i in range(N):
  cmd = sys.stdin.readline().split()
  if cmd[0] == "pop":
    if len(queue) == 0: 
      print(-1)
    else:
      top = queue[0]
      del queue[0]
      print(top)
  elif cmd[0] == "size":
    print(len(queue))
  elif cmd[0] == "empty":
    if (len(queue) == 0): print(1)
    else: print(0)
  elif cmd[0] == "front":
    if (len(queue) == 0): print(-1)
    else: print(queue[0])
  elif cmd[0] == "back":
    if (len(queue) == 0): print(-1)
    else: print(queue[-1])
  else:
    arg = cmd[1]
    queue.append(arg)