# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """res=[]
        return self.fun(root,res)"""


        # Iterative Solution...
        if root==None:
            return []
        st=[root]
        ans=[]
        while st:
            temp=st.pop()
            ans.append(temp.val)
            if temp.right!=None:
                st.append(temp.right)
            if temp.left!=None:
                st.append(temp.left)
        return ans  



    """def fun(self,node,res):
        if node==None:
            return [] 
        res.append(node.val)
        self.fun(node.left,res)
        self.fun(node.right,res)
        return res"""

        