from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if node is None:
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = deque([int(val) for val in data.split(",")] if data else [])

        def dfs(lower, upper):
            if not vals:
                return None
            if not (lower < vals[0] < upper):
                return None

            node = TreeNode(vals.popleft())
            node.left = dfs(lower, node.val)
            node.right = dfs(node.val, upper)
            return node

        return dfs(float("-inf"), float("inf"))
