class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node, val):
        if val < node.val:
            if node.left:
                self._insert(node.left, val)
            else:
                node.left = TreeNode(val)
        else:
            if node.right:
                self._insert(node.right, val)
            else:
                node.right = TreeNode(val)

    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if not node:
            return node
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self._minValueNode(node.right)
            node.val = temp.val
            node.right = self._delete(node.right, temp.val)

        return node

    def _minValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def inorderTraversal(self):
        result = []
        self._inorderTraversal(self.root, result)
        return result

    def _inorderTraversal(self, node, result):
        if not node:
            return
        self._inorderTraversal(node.left, result)
        result.append(node.val)
        self._inorderTraversal(node.right, result)

# Example Usage
bst = BST()
nodes = [50, 30, 20, 40, 70, 60, 80]
for node in nodes:
    bst.insert(node)

print("Inorder traversal before deletion:", bst.inorderTraversal())
bst.delete(50)
print("Inorder traversal after deletion:", bst.inorderTraversal())
