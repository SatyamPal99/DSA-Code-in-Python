# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0

        lh=self.left_height(root)
        rh=self.right_height(root)
        if lh==rh:
            return (2**lh-1)
        return 1+self.countNodes(root.left)+self.countNodes(root.right)


    def left_height(self,root):
        lh=0
        while root:
            lh+=1
            root=root.left
        return lh

    def right_height(self,root):
        rh=0
        while root:
            rh+=1
            root=root.right
        return rh
        