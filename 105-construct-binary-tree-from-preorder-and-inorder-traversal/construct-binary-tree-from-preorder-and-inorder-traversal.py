# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map={}
        for i in range(len(inorder)):
            if inorder[i] not in inorder_map:
                inorder_map[inorder[i]]=i
        ans=self.fun(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1,inorder_map)
        return ans


    def fun(self,preorder,pre_start,pre_end,inorder,in_start,in_end,mapp):
        if pre_start>pre_end or in_start>in_end:
            return None
        root=TreeNode(preorder[pre_start])
        in_root=mapp[root.val]
        left_nums=in_root-in_start
        root.left=self.fun(preorder,pre_start+1,pre_start+left_nums,inorder,in_start,in_root-1,mapp)
        root.right=self.fun(preorder,pre_start+left_nums+1,pre_end,inorder,in_root+1,in_end,mapp)
        return root
