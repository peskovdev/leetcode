from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        p_ancestors = self.get_ancestors(root, p)
        q_ancestors = self.get_ancestors(root, q)
        for p_anc in p_ancestors:
            for q_anc in q_ancestors:
                if p_anc is q_anc:
                    return p_anc

    def get_ancestors(self, root: Optional["TreeNode"], subtree: TreeNode, ancestors: list = []):
        if root is None:
            return []

        if subtree is root:
            return [root]

        res = self.get_ancestors(root.left, subtree)
        if len(res) > 0:
            res.append(root)
            return res
        else:
            res = self.get_ancestors(root.right, subtree)
            if len(res) > 0:
                res.append(root)
                return res

        return []
