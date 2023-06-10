from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<val={self.val},left={self.left},right={self.right}>"


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if root:
            if root.left is None or root.right is None:
                return False
            return root.val == root.left.val + root.right.val
        return False


sol = Solution()

subtree11 = TreeNode(val=4, left=2, right=8)
subtree12 = TreeNode(val=6, left=5, right=2)
tree1 = TreeNode(val=10, left=subtree11, right=subtree12)
print(sol.checkTree(tree1))

subtree21 = TreeNode(val=3, left=0, right=5)
subtree22 = TreeNode(val=1, left=3, right=7)
tree2 = TreeNode(val=5, left=subtree11, right=subtree12)
print(sol.checkTree(tree2))

cut_tree = TreeNode(val=5)
print(sol.checkTree(cut_tree))
