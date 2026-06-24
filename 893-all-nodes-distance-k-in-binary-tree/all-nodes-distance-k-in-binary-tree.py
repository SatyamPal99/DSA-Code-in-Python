# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        mapp={}
        self.parent_find(root,mapp)
        tar_root=target
        visited=[]
        q=deque()
        q.append(tar_root)
        dis=0
        visited.append(tar_root)
        while q:
            if dis==k:
                return [i.val for i in q]
            for j in range(len(q)): 
                temp=q.popleft()
                if temp.left and temp.left not in visited:
                    q.append(temp.left)
                    visited.append(temp.left)
                if temp.right and temp.right not in visited:
                    q.append(temp.right)
                    visited.append(temp.right)
                if temp in mapp and mapp[temp] not in visited:
                    q.append(mapp[temp])
                    visited.append(mapp[temp])
            dis+=1
        return []



    """def find_target(self,root,tar):
        if root==None:
            return 
        if root==tar:
            return root
        ans1=self.find_target(root.left,tar)
        ans2=self.find_target(root.right,tar)
        return ans1 if ans1 else ans2"""
        

    def parent_find(self,root,mapp):
        q=deque()
        q.append(root)
        while q:
            temp=q.popleft()
            if temp.left:
                mapp[temp.left]=temp
                q.append(temp.left)
            if temp.right:
                mapp[temp.right]=temp
                q.append(temp.right)
            
            
        