from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []

        res: list[list[int]] = []
        stack: list[TreeNode] = []
        stack.append(root)
        while stack:
            new_stack = []
            res.append([])
            for node in stack:
                res[-1].append(node.val)
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            stack = new_stack
        return res
