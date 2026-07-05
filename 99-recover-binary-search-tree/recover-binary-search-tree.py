# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        ans=[]
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
        return self.helper(root,ans)

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

