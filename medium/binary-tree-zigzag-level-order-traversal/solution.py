from typing import Optional, Deque
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        res: list[list[int]] = []
        q: Deque[TreeNode] = deque([root] if root else [])
        while q:
            res.append([])
            for _ in range(len(q)):
                if len(res) % 2 == 0:
                    node = q.popleft()
                    if node.right:
                        q.append(node.right)
                    if node.left:
                        q.append(node.left)
                else:
                    node = q.pop()
                    if node.left:
                        q.appendleft(node.left)
                    if node.right:
                        q.appendleft(node.right)
                res[-1].append(node.val)
        return res
