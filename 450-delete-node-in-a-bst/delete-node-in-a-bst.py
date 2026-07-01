# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root==None:
            return None
        if root.val==key:
            return self.helper(root,key)
        dummy=root
        while root:
            if root.val>key:
                if root.left!=None and root.left.val==key:
                    root.left=self.helper(root.left,key)
                else:
                    root=root.left
            else:
                if root.right!=None and root.right.val==key:
                    root.right=self.helper(root.right,key)
                else:
                    root=root.right
        return dummy
    

    def helper(self,root,k):
        if root.left==None:
            return root.right
        if root.right==None:
            return root.left
        rightchild=root.right
        lastRight=self.find(root.left)
        lastRight.right=rightchild
        return root.left

    def find(self,root):
        if root.right==None:
            return root
        ans=self.find(root.right)
        return ans
        