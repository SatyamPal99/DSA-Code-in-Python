# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """ans=[]
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
        return pred"""




        if not root:
            return False

        asc  = []   # inorder iterator (small → large)
        desc = []   # reverse inorder iterator (large → small)

        # initialize asc with leftmost path
        t = root
        while t:
            asc.append(t)
            t = t.left

        # initialize desc with rightmost path
        t = root
        while t:
            desc.append(t)
            t = t.right

        def getSmall():
            if not asc:
                return None
            small = asc.pop()
            node = small.right      # explore right subtree
            while node:
                asc.append(node)
                node = node.left
            return small

        def getBig():
            if not desc:
                return None
            big = desc.pop()
            node = big.left         # explore left subtree
            while node:
                desc.append(node)
                node = node.right
            return big

        i = getSmall()              # points to smallest
        j = getBig()                # points to largest

        while i and j and i != j and i.val < j.val:
            total = i.val + j.val
            if total == k:
                return True
            elif total > k:
                j = getBig()
            else:
                i = getSmall()

        return False