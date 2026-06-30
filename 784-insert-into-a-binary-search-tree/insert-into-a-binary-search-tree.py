# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root==None:
            return TreeNode(val,None,None)
        temp=root
        while temp:
            if temp.left==None and val<temp.val:
                new=TreeNode(val,None,None)
                temp.left=new
                return root
            elif temp.right==None and val>temp.val:
                new=TreeNode(val,None,None)
                temp.right=new
                return root
            if val>temp.val:
                temp=temp.right
            else:
                temp=temp.left
        
        return root

        