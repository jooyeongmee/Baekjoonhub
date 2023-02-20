import sys
from itertools import combinations

def get_brackets(input):
  stack = []
  bstack = []
  for i in range(len(input)):
    # print(i, len(input))

    if input[i] == "(":
      stack.append(i)
    elif input[i] == ")":
      bstack.append((stack.pop(), i))
  return bstack

input = list(sys.stdin.readline().strip())

answer = []  

brackets = get_brackets(input)

for i in range(len(brackets)):
  target_list = list(combinations(brackets, i+1))
  # print(target_list)
  for target in target_list:
    # print(target)
    temp = input[:]
    for t in target:
      # print(t[0], t[1])
      temp[t[0]] = ""
      temp[t[1]] = ""
    answer.append(''.join(temp))

[print(_) for _ in sorted(set(answer))]


 