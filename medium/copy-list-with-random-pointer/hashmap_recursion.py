from typing import Optional


class Node:
    def __init__(self, x: int, next: "Optional[Node]" = None, random: "Optional[Node]" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return None

        hashmap: dict[Node, Node] = {}

        def recurse(head: Node):
            cp_head = Node(x=head.val, next=None, random=None)
            hashmap[head] = cp_head
            if head.next:
                cp_head_next = recurse(head.next)
                cp_head.next = cp_head_next
            if head.random is not None:
                cp_head.random = hashmap[head.random]
            return cp_head

        return recurse(head)
