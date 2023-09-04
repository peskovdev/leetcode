from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


hashset = set()


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head in hashset:
            return True
        hashset.add(head)
        if head and head.next is not None:
            result = self.hasCycle(head.next)
            return result
        return False
