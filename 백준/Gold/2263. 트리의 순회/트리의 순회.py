import sys
sys.setrecursionlimit(10**6)

#입력받은 inorder 리스트를 key=값, value=인덱스 형식의 디셔너리로 만들고 반환한다.
def insert_data(inorder):
  dict = {}
  for i, val in enumerate(inorder):
    dict[val] = i
  return dict

N = int(input())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))

#key가 정수 값이고 value가 그 정수가 inorder 리스트에서의 인덱스인 딕셔너리이다.
inorder_dict = insert_data(inorder)

#in_start: inorder에서 시작 인덱스, in_end: inorder에서 마지막 인덱스
#post_start: postorder에서 시작 인덱스, post_end: postorder에서 마지막 인덱스
#항상 루트는 postorder에서 마지막 인덱스가. 루트가 젤 마지막에 출력되기 때문
#postorder에서 루트를 찾고 그 루트가 inorder에서의 인덱스를 inorder_dict를 통해 찾는다.
# inorder 리스트에서 찾은 인덱스의 왼쪽부분은 루트의 left subtree 이고 오른쪽 부분은 루트의 right subtree이다.
#그러면 다시 인덱스 조정을 하여 left subtree, right_subtree를 재귀로 돌린다.
def print_preorder(in_start, in_end, post_start, post_end):
  # print(inorder[in_start:in_end+1], postorder[in_start:in_end+1])
  if (in_start > in_end) or (post_start > post_end): return
    
  root = postorder[post_end]
  print(root, end =" ")
  
  length = inorder_dict[root] - in_start
  
  print_preorder(in_start,  inorder_dict[root]- 1, post_start, post_start + length - 1)
  print_preorder(inorder_dict[root] + 1, in_end, post_start + length, post_end - 1)

print_preorder(0, N-1, 0, N-1)
 