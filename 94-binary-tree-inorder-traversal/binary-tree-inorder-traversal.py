# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        return self.fun(root,res)
    def fun(self,node,res):
        if node==None:
            return []
        self.fun(node.left,res)
        res.append(node.val)
        self.fun(node.right,res)
        return res
        