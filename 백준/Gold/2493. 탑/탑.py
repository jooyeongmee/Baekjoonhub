import sys

N = int(input())
input = sys.stdin.readline().split()
result = [0 for _ in range(N)]

stack = []
stack.append(0)
for i in range(1, N):
  while len(stack) != 0:
    if int(input[stack[-1]]) < int(input[i]):
      stack.pop()
    else:
      result[i] = stack[-1] + 1
      break
  stack.append(i)

print(" ".join(map(str, result)))