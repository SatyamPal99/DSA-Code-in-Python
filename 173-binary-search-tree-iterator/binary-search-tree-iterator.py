# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    """def __init__(self, root: Optional[TreeNode]):
        self.st=[]
        self.pushAll(root)
        
    def next(self) -> int:
        node=(self.st.pop())
        self.pushAll(node.right)
        return node.val

    def hasNext(self) -> bool:
        if self.st:
            return True
        else:
            return False

    def pushAll(self,root):
        while root:
            self.st.append(root)
            root=root.left"""
    

    def __init__(self, root: Optional[TreeNode]):
        self.values = []
        self.idx = 0
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.values.append(node.val)
            inorder(node.right)

        inorder(root)        

    def next(self) -> int:
        val = self.values[self.idx]
        self.idx += 1
        return val

    def hasNext(self) -> bool:
        return len(self.values) > self.idx
        

        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()