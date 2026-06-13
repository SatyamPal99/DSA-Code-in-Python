# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        q=deque()
        q.append(root)
        res=[]
        while q:
            ans=[]
            for i in range(len(q)):
                temp=q.popleft()
                ans.append(temp.val)
                if temp.left!=None:
                    q.append(temp.left)
                if temp.right!=None:
                    q.append(temp.right)
            res.append(ans)
        return res
            
        