from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        q = deque([root])

        while q:
            node = q.popleft()
            if node is None:
                continue
            if low <= node.val <= high:
                res += node.val
            if low < node.val:
                q.append(node.left)
            if high > node.val:
                q.append(node.right)

        return res
