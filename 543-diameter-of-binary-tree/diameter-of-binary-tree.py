# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        self.dia=-math.inf #instace variable(global var) it belongs to solution class so every 
                              #                      method in this class can use it.
        self.fun(root)
        return self.dia

    def fun(self,root):
        if root==None:
            return 0
        left=self.fun(root.left)
        right=self.fun(root.right)
        self.dia=max(self.dia,left+right)
        return 1+max(left,right)
        