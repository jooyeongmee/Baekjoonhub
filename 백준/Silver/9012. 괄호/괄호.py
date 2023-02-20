import sys

T = int(input())

for i in range(T):
  input = sys.stdin.readline().strip()
  stack = []
  answer = "YES"
  for i in range(len(input)):
    if input[i] == "(":
      stack.append(input[i])
    else:
      if len(stack) > 0 and stack[-1] == "(":
        stack.pop()
      else:
        answer = "NO"
        break;
  if len(stack) > 0:
    answer = "NO"
  print(answer)

    
