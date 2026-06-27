# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """res=[]
        return self.fun(root,res)"""

        # Morris Traversal

        ans=[]
        curr=root
        while curr:
            if curr.left==None:
                ans.append(curr.val)
                curr=curr.right
            else:
                predecessor=self.find_p(curr)
                if predecessor.right is None:
                    predecessor.right=curr
                    curr=curr.left
                else:
                    predecessor.right=None
                    ans.append(curr.val)
                    curr=curr.right
        return ans

    def find_p(self,curr):
        pred=curr.left
        while pred.right and pred.right!=curr:
            pred=pred.right
        return pred




    def fun(self,node,res):
        if node==None:
            return []
        self.fun(node.left,res)
        res.append(node.val)
        self.fun(node.right,res)
        return res
        