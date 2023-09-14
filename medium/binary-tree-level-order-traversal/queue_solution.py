from typing import Optional, Deque
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        res: list[list[int]] = []
        q: Deque[TreeNode] = deque()
        if root:
            q.append(root)

        while q:
            res.append([])
            for _ in range(len(q)):
                node = q.popleft()
                res[-1].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
