import sys

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def insert_data(tree, data):
  node = Node(data[0])
  if data[1] != '.': 
    node.left = Node(data[1])
  if data[2] != '.': 
    node.right = Node(data[2])
  tree[data[0]] = node
  return tree

def preorder(tree, node):
  if node == None: return
  print(node.value, end='')
  preorder(tree, tree[node.value].left)
  preorder(tree, tree[node.value].right)

def inorder(tree, node):
  if node == None: return
  inorder(tree, tree[node.value].left)
  print(node.value, end='')
  inorder(tree, tree[node.value].right)

def postorder(tree, node):
  if node == None: return
  postorder(tree, tree[node.value].left)
  postorder(tree, tree[node.value].right)
  print(node.value, end='')
  

N = int(input())
tree = {}
tree["root"] = Node('A')
for i in range(N):
  data = sys.stdin.readline().split()
  tree = insert_data(tree, data)

preorder(tree, tree["root"])
print()
inorder(tree, tree["root"])
print()
postorder(tree, tree["root"])
