import sys

N = int(input())
input_str = sys.stdin.readline().strip()
args = [sys.stdin.readline().strip() for _ in range(N)] 

stack = []

for i in range(len(input_str)):
  if input_str[i] == '*':
    top1 = stack.pop()
    top2 = stack.pop()
    stack.append(top1 * top2)
  elif input_str[i] == '+':
    top1 = stack.pop()
    top2 = stack.pop()
    stack.append(top1 + top2)
  elif input_str[i] == '-':
    top1 = stack.pop()
    top2 = stack.pop()
    stack.append(top2 - top1)
  elif input_str[i] == '/':
    top1 = stack.pop()
    top2 = stack.pop()
    stack.append(top2 / top1)
  else:
    if input_str[i].isalpha():
      stack.append(int(args[ord(input_str[i]) - 65]))
    
print("{:.2f}".format(stack[0]))

