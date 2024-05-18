class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def tra_preorder(self, root):
        if root:
            print(root.val, end=' ')
            self.tra_preorder(root.left)
            self.tra_preorder(root.right)

    def tra_postorder(self, root):
        if root:
            self.tra_postorder(root.left)
            self.tra_postorder(root.right)
            print(root.val, end=' ')

    def tra_inorder(self, root):
        if root:
            self.tra_inorder(root.left)
            print(root.val, end=' ')
            self.tra_inorder(root.right)

# Create the tree structure
root = Node(2)
root.left = Node(3)
root.right = Node(4)
root.right.left = Node(7)
root.right.right = Node(8)
root.left.left = Node(5)
root.left.left.left = Node(9)
root.right.right = Node(6)

# Perform the traversals
print("Inorder traversal")
root.tra_inorder(root)
print("\nPreorder traversal")
root.tra_preorder(root)
print("\nPostorder traversal")
root.tra_postorder(root)
