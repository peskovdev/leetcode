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

        res = 0
        stack = [(root, 1, {root.left, root.right})]

        while stack:
            node, depth, not_checked = stack[-1]
            res = max(res, depth)

            left = node.left
            right = node.right

            if left and left in not_checked:
                stack.append((left, depth + 1, {left.left, left.right}))
                not_checked.remove(left)
                continue
            if right and right in not_checked:
                stack.append((right, depth + 1, {right.left, right.right}))
                not_checked.remove(right)
                continue
            stack.pop()

        return res
