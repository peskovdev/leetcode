from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node: Optional[TreeNode], left=False):
            if node is None:
                return
            dfs(node.left, left=True)
            dfs(node.right)
            if node.left is node.right is None and left:
                self.res += node.val

        dfs(root)
        return self.res
