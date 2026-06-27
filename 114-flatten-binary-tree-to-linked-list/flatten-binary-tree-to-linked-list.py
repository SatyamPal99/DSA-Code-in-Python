# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:

        arr = []

        self.preorder(root, arr)

        for i in range(len(arr) - 1):
            arr[i].left = None
            arr[i].right = arr[i + 1]

        if arr:
            arr[-1].left = None
            arr[-1].right = None

    def preorder(self, root, arr):

        if root is None:
            return

        arr.append(root)

        self.preorder(root.left, arr)
        self.preorder(root.right, arr)