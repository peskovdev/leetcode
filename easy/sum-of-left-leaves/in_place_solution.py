from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        res = self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        if root.left and root.left.left is root.left.right is None:
            res += root.left.val

        return res
