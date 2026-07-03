# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        mini=-(math.inf)
        maxi=math.inf
        return self.fun(root,mini,maxi)
    def fun(self,root,mini,maxi):
        if root==None:
            return True
        ans1=self.fun(root.left,mini,root.val)
        ans2=self.fun(root.right,root.val,maxi)
        temp=(ans1 and ans2)
        if mini<root.val<maxi:
                return True and temp
        else:
            return False and temp
        