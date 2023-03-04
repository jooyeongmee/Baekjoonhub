import sys
sys.setrecursionlimit(10**6)

k = int(input())
inorder = sys.stdin.readline().split()

size = pow(2, k) - 1

arr=[[] for _ in range(k)]

def make_tree(in_start, in_end, count):
  if in_start >= in_end: return
    
  idx = (in_start + in_end) // 2
  root = inorder[idx]
  arr[count].append(root)
  
  make_tree(in_start,  idx, count+1)
  make_tree(idx+1, in_end, count+1)

make_tree(0, size, 0)

for _ in arr:
  print(" ".join(_))