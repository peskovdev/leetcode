class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        a = root

        def dfs(root):
            if self.contain_tree(root, p) and self.contain_tree(root, q):
                nonlocal a
                a = root
                dfs(root.left)
                dfs(root.right)
            return False
        dfs(root)
        return a

    def contain_tree(self, root, subtree):
        if root is subtree:
            return True
        if root is None:
            return False

        return self.contain_tree(root.left, subtree) or self.contain_tree(root.right, subtree)
