class Node:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None


# Preorder Traversal
# Root -> Left -> Right
def preorder(root):

    if root is None:
        return

    print(root.val, end=" ")

    preorder(root.left)
    preorder(root.right)


# Inorder Traversal
# Left -> Root -> Right
def inorder(root):

    if root is None:
        return

    inorder(root.left)

    print(root.val, end=" ")

    inorder(root.right)


# Postorder Traversal
# Left -> Right -> Root
def postorder(root):

    if root is None:
        return

    postorder(root.left)

    postorder(root.right)

    print(root.val, end=" ")


# -------- Creating Tree --------

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

# Tree Structure:
#
#         1
#        / \
#       2   3
#      / \
#     4   5


# -------- Traversals --------

print("Preorder Traversal:")
preorder(root)

print("\nInorder Traversal:")
inorder(root)

print("\nPostorder Traversal:")
postorder(root)