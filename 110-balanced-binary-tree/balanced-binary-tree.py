# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        l=self.Height(root.left)
        r=self.Height(root.right)
        if abs(l-r)>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def Height(self,node):
        if node==None:
            return 0
        l=self.Height(node.left)
        r=self.Height(node.right)
        return 1+max(l,r)
        