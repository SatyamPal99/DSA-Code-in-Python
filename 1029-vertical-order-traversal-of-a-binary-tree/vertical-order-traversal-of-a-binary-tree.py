from collections import defaultdict , deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mapp = defaultdict(lambda:defaultdict(list)) # if a key not present then append emptylist        
        q=deque([(root,(0,0))]) #list of tuples inside queue
        while q:
            node,(x,y)=q.popleft()
            mapp[x][y].append(node.val)
            if node.left:
                q.append((node.left,(x-1,y+1)))
            if node.right:
                q.append((node.right,(x+1,y+1)))
        ans=[]
        for x in sorted(mapp):   #sorting on the basis of x(or vertical values)
            col=[]
            for y in sorted(mapp[x]):   # sorting inside x on the basis of y...
                col.extend(sorted(mapp[x][y]))   # append value on nested key [x][y]--> value
            ans.append(col)
        return ans