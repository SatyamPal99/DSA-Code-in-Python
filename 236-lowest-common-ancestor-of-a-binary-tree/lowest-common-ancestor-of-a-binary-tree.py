# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        #Bruteforce

        """ans=[]
        temp=[]
        self.fun(root,p,q,temp,ans)
        lis1=ans[0]
        lis2=ans[1]
        i=0
        j=0
        while i<len(lis1) and j<len(lis2):
            if lis1[i]!=lis2[j]:
                return lis1[i-1]
            i+=1
            j+=1
        return lis1[i-1]

    def fun(self,root,p,q,temp,ans):
        if root==None:
            return
        temp.append(root)
        if root.val==p.val or root.val==q.val:
            ans.append(temp[:])


        self.fun(root.left,p,q,temp,ans)
        self.fun(root.right,p,q,temp,ans)
        temp.pop()"""


        # Optimized Approach....

        if root==None or root==p or root==q:
            return root

        
        ans1=self.lowestCommonAncestor(root.left,p,q)
        ans2=self.lowestCommonAncestor(root.right,p,q)
        if ans1==None:
            return ans2
        elif ans2==None:
            return ans1
        else:
            return root