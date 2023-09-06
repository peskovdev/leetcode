from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0

            left, right = dfs(root.left), dfs(root.right)

            if abs(left - right) > 1:
                nonlocal res
                res = False

            return 1 + max(left, right)

        dfs(root)
        return res
