# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        q=deque()
        q.append((0,root))
        mapp={}
        while q:
            temp=q.popleft()
            level=temp[0]
            data=temp[1]
            if level not in mapp:
                mapp[level]=data.val
            if data.right:
                q.append((level+1,data.right))
            if data.left:
                q.append((level+1,data.left))
        ans=[]
        for i in sorted(mapp):
            ans.append(mapp[i])
        return ans