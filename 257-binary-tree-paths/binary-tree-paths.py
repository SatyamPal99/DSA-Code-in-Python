# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans=[]
        temp=[]
        self.fun(root,ans,temp)
        return ans

    #using inorder traversal...
    def fun(self,root,ans,temp):
        if root==None:
            return 
        temp.append(root.val)

        if root.left==None and root.right==None:
            res="->".join(map(str,temp))
            ans.append(res)
            temp.pop()
            return

        self.fun(root.left,ans,temp)
        self.fun(root.right,ans,temp)
        temp.pop()

        
        