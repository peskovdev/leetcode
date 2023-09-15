from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode], lower=float("-inf"), greater=float("inf")) -> bool:
        if root is None:
            return True

        if lower >= root.val or root.val >= greater:
            return False

        is_valid_left = self.isValidBST(root.left, lower, root.val)
        is_valid_right = self.isValidBST(root.right, root.val, greater)
        return is_valid_left and is_valid_right
