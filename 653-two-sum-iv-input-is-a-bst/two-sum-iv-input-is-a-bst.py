# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        ans=[]
        dummy=root
        while root:
            if root.left==None:
                ans.append(root.val)
                root=root.right
            else:
                pred=self.find_p(root)
                if pred.right==None:
                    pred.right=root
                    root=root.left
                else:
                    ans.append(root.val)
                    pred.right=None
                    root=root.right
        low=0
        high=len(ans)-1
        while(low<high):
            if ans[low]+ans[high]==k:
                return True
            elif ans[low]+ans[high]<k:
                low+=1
            else:
                high-=1
        return False


    def find_p(self,root):
        pred=root.left
        while pred.right and pred.right!=root:
            pred=pred.right
        return pred
        