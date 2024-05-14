class Node:
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data
class left_skewed:
    def insert1(self,root,data):
        if root is None:
            root=Node(data)
        else:
            root.left=self.insert1(root.left,data)
        return root
    def print_tree(self,root):
        if root:
            if root.data :
                print(root.data)
                self.print_tree(root.left)
root=None
obj=left_skewed()
root=obj.insert1(root,1)
root=obj.insert1(root,3)
root=obj.insert1(root,4)
root=obj.insert1(root,5)
root=obj.insert1(root,6)
root=obj.insert1(root,7)
obj.print_tree(root)
