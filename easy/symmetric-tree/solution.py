from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def cross_dfs(q: Optional[TreeNode], p: Optional[TreeNode]) -> bool:
            if q is p is None:
                return True
            if q is None or p is None or q.val != p.val:
                return False
            return cross_dfs(q.left, p.right) and cross_dfs(q.right, p.left)

        return cross_dfs(root.left, root.right)
