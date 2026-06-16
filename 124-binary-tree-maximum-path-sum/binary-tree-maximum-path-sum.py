# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.sum=-math.inf
        self.fun(root)
        return self.sum
    def fun(self,root):
        if root==None:
            return 0
        l=self.fun(root.left)
        r=self.fun(root.right)
        niche_hi_answer_milgaya=l+r+root.val
        koi_ek_acha=max(l,r)+root.val
        sirf_root_acha=root.val
        self.sum=max(self.sum,niche_hi_answer_milgaya,koi_ek_acha,sirf_root_acha)
        return max(koi_ek_acha,sirf_root_acha)