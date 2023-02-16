import sys

N = int(input())
stack = []
for i in range(N):
  cmd = sys.stdin.readline().split()
  if cmd[0] == "pop":
    if len(stack) == 0: 
      print(-1)
    else:
      top = stack.pop()
      print(top)
  elif cmd[0] == "size":
    print(len(stack))
  elif cmd[0] == "empty":
    if (len(stack) == 0): print(1)
    else: print(0)
  elif cmd[0] == "top":
    if (len(stack) == 0): print(-1)
    else: print(stack[-1])
  else:
    arg = cmd[1]
    stack.append(arg)