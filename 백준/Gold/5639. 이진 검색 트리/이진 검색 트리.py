import sys

sys.setrecursionlimit(10 ** 6)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class tree:
    def __init__(self):
        self.root = None

    def insert(self, node):
        if self.root == None:
            self.root = node
        else:

            current = self.root
            while current != None:
                if node.value < current.value:
                    if current.left == None:
                        current.left = node
                        break
                    else:
                        current = current.left
                else:
                    if current.right == None:
                        current.right = node
                        break
                    else:
                        current = current.right


def postorder(current):
    if current == None: return
    postorder(current.left)
    postorder(current.right)
    print(current.value)


tree = tree()
while True:
    val = sys.stdin.readline().strip()
    if not val: break
    tree.insert(Node(int(val)))

postorder(tree.root)