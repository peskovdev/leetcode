from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> list[Optional[TreeNode]]:
        hashmap: dict[str, int] = {}
        res: list[Optional[TreeNode]] = []

        def dfs(root):
            if root is None:
                return ""

            s = ",".join([str(root.val), dfs(root.left), dfs(root.right)])
            if s in hashmap and hashmap[s] == 1:
                res.append(root)
            hashmap[s] = hashmap.get(s, 0) + 1
            return s

        dfs(root)
        return res
