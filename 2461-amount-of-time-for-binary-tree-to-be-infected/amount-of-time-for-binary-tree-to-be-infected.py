# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        mapp={}
        self.parent(root,mapp)
        node=self.find_Node(root,start)
        visited=set()   # search in set is O(1) and list is O(n)
        visited.add(node)
        res=0
        q=deque()
        q.append(node)
        while q:
            size=len(q)
            for i in range(size):
                temp=q.popleft()
                if temp.left and temp.left not in visited:
                    q.append(temp.left)
                    visited.add(temp.left)
                if temp.right and temp.right not in visited:
                    visited.add(temp.right)
                    q.append(temp.right)
                if temp in mapp and mapp[temp] not in visited:
                    visited.add(mapp[temp])
                    q.append(mapp[temp])
            res+=1
        return res-1
    
    def find_Node(self,root,start):
        if root==None:
            return 
        if root.val==start:
            return root

        a1=self.find_Node(root.left,start)
        a2=self.find_Node(root.right,start)
        if a1!=None:
            return a1
        else:
            return a2 


    def parent(self,root,mapp):
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
        
        