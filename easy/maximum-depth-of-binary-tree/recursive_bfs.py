from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        depth = 0

        def recurese_bfs(tries: list[TreeNode]):
            nonlocal depth
            depth += 1
            children: list[TreeNode] = []
            for node in tries:
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)

            if children:
                recurese_bfs(children)

        recurese_bfs([root])
        return depth
