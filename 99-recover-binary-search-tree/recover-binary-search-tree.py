# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        # Bruteforce Approach
        """ans=[]
        q=deque([root])
        while q:
            temp=q.popleft()
            ans.append(temp.val)
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        ans.sort()
        print(ans)
        return self.helper(root,ans)"""

        # Optimized Approach....

        self.first=None
        self.middle=None
        self.last=None
        self.prev=None
        self.fun(root)
        if self.first and self.last:
            self.first.val,self.last.val=self.last.val,self.first.val
        else:
            self.first.val,self.middle.val=self.middle.val,self.first.val
        


    def fun(self,root):
        if root==None:
            return
        self.fun(root.left)
        if self.prev!=None and self.prev.val>root.val:
            if self.first==None:
                self.first=self.prev
                self.middle=root
            else:
                self.last=root
        self.prev=root

        self.fun(root.right)
        


    def helper(self,root,ans):
        curr=root
        i=0
        while root:
            if root.left==None:
                if ans[i]!=root.val:
                    root.val=ans[i]
                i+=1
                root=root.right
            else:
                pred=self.find_pred(root)
                if pred.right==None:
                    pred.right=root 
                    root=root.left
                else:
                    if ans[i]!=root.val:
                        root.val=ans[i]
                    i+=1
                    pred.right=None
                    root=root.right
        
        return curr


    def find_pred(self,root):
        pred=root.left
        while pred.right and pred.right!=root:
            pred=pred.right
        return pred

