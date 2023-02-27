import sys

def check_str(str):
  result = False
  for s in str:
    if ord(s) < 32 or ord(s) > 126:
      result = True
  return result
dict = {}
count = 0
while True:
  tree = sys.stdin.readline().strip()
  if check_str(tree):
    break
  if not tree:
    break
  count += 1
  if tree in dict.keys():
    dict[tree] += 1
  else:
    dict[tree] = 1

for key in dict.keys():
  dict[key] = dict[key] * 100 / count

sorted_dict = sorted(dict.items())

for _ in sorted_dict:
  print(f'{_[0]} {_[1]:.4f}')
