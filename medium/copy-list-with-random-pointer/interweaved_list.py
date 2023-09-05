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

        cur = head
        while cur:
            duplicate = Node(x=cur.val, next=cur.next, random=cur.random)
            cur.next = duplicate
            cur = duplicate.next

        cur = head
        while cur:
            duplicate = cur.next
            if duplicate.random is not None:
                duplicate.random = duplicate.random.next
            cur = duplicate.next
            if duplicate.next:
                duplicate.next = duplicate.next.next

        return head.next
