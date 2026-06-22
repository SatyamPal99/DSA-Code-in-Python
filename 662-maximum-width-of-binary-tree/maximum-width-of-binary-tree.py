# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=0
        q=deque()
        q.append((root,0))
        while q:
            size=len(q)
            first=-1
            last=-1
            minn=q[0][1]
            for i in range(size):
                temp=q.popleft()
                idx=temp[1]
                node=temp[0]
                cur_idx=idx-minn
                if i==0:
                    first=cur_idx
                if i==size-1:
                    last=cur_idx
                if node.left:
                    q.append((node.left,cur_idx*2+1))
                if node.right:
                    q.append((node.right,cur_idx*2+2))
            ans=max(ans,last-first+1)
        return ans

