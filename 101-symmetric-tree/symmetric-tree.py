# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """if root==None or (root.left==None and root.right==None):
            return True
        if root.left==None or root.right==None:
            return False
        q1=deque()
        q2=deque()
        q1.append((root.left,-1))
        q2.append((root.right,1))
        while q1 and q2:
            temp1=q1.popleft()
            node1=temp1[0]
            x1=temp1[1]
            temp2=q2.popleft()
            node2=temp2[0]
            x2=temp2[1]
            if node1.val!=node2.val or abs(x1+x2)!=0 or len(q1)!=len(q2):
                return False
            if node1.left:
                q1.append((node1.left,x1-1))
            if node1.right:
                q1.append((node1.right,x1+1))
            if node2.right:
                q2.append((node2.right,x2+1))
            if node2.left:
                q2.append((node2.left,x2-1))
        return True"""
        if root.left==root.right==None:
            return True
        if (root.left==None or root.right==None):
            return False

        if root.left.val!=root.right.val:
            return False
        return self.fun(root.left,root.right)
    def fun(self,left_root,right_root):
        if left_root==None or right_root==None:
            return left_root == right_root
   
        if left_root.val!=right_root.val:
            return False
        t1=self.fun(left_root.left,right_root.right)
        t2=self.fun(left_root.right,right_root.left)
        return t1 and t2


        