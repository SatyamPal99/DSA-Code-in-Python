# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:


        # Bruteforce - time=O(n)  space = O(n)
        """arr = []
        self.preorder(root, arr)
        for i in range(len(arr) - 1):
            arr[i].left = None
            arr[i].right = arr[i + 1]
        if arr:
            arr[-1].left = None
            arr[-1].right = None"""

        # using Recusion tail approach...
        """self.helper(root)"""

        # using Morris Traversal 
        curr=root
        while curr:
            if curr.left:
                prev=curr.left
                while prev.right:
                    prev=prev.right
                prev.right=curr.right
                curr.right=curr.left
                curr.left=None
            curr=curr.right
        





    """def helper(self,root):
        if root==None:
            return None
        
        left_tail=self.helper(root.left)
        right_tail=self.helper(root.right)

        if left_tail:
            left_tail.right=root.right
            root.right=root.left
            root.left=None
        if right_tail:
            return right_tail
        if left_tail:
            return left_tail
        return root

    def preorder(self, root, arr):
        if root is None:
            return

        arr.append(root)
        self.preorder(root.left, arr)
        self.preorder(root.right, arr)"""