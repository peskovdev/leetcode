from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        q = deque([root] if root else [])
        res = []
        while q:
            node = q.popleft()
            res.append(str(node.val) if node else "null")
            if node:
                q.append(node.left)
                q.append(node.right)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None

        vals = deque(data.split(","))
        i = 0
        root = None if vals[i] == "null" else TreeNode(int(vals[i]))
        head = root

        q = deque([root] if root else [])
        while q:
            root = q.popleft()

            i += 1
            root.left = None if vals[i] == "null" else TreeNode(int(vals[i]))
            i += 1
            root.right = None if vals[i] == "null" else TreeNode(int(vals[i]))

            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
        return head
