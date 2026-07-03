# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # Optimized Approach...
        upper_bound=math.inf
        self.i=0
        return self.helper(preorder,upper_bound)

    def helper(self,pre,ub):
        if self.i>=len(pre) or pre[self.i]>ub:
            return None

        node=TreeNode(pre[self.i])
        self.i+=1
        node.left=self.helper(pre,node.val)
        node.right=self.helper(pre,ub)
        return node
        






        """inorder=sorted(preorder)
        mapp={}
        for i in range(len(inorder)):
            if inorder[i] not in mapp:
                mapp[inorder[i]]=i
        return self.fun(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1,mapp)
        
    def fun(self,pre,preSt,preEnd,inorder,inSt,inEnd,mapp):
        if preSt>preEnd or inSt>inEnd:
            return None
        node=TreeNode(pre[preSt])
        in_root=mapp[node.val]
        left_nums=in_root-inSt
        node.left=self.fun(pre,preSt+1,left_nums+preSt,inorder,inSt,in_root-1,mapp)
        node.right=self.fun(pre,left_nums+preSt+1,preEnd,inorder,in_root+1,inEnd,mapp)
        return node"""

        