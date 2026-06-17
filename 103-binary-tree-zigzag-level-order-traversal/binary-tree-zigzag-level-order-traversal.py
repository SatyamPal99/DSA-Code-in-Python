# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=deque()
        q.append(root)
        flag=False
        ans=[]
        while q:
            size=len(q)
            res=[0]*len(q)
            for i in range(len(q)):
                temp=q.popleft()
                idx=i if flag else size-i-1
                res[idx]=temp.val
                if temp.right:
                    q.append(temp.right)
                if temp.left:
                    q.append(temp.left)
            flag=not flag
            ans.append(res)
        return ans

                


        