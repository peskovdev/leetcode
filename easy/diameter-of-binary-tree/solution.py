from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root: Optional[TreeNode]):
            if root is None:
                return 0

            left_depth = dfs(root.left)
            right_depth = dfs(root.right)

            nonlocal res
            res = max(res, left_depth + right_depth)

            return 1 + max(left_depth, right_depth)

        dfs(root)
        return res
