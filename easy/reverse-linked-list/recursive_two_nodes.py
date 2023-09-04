from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recursion(prev: Optional[ListNode], current: Optional[ListNode]) -> Optional[ListNode]:
            if current is None:
                return prev

            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

            head = recursion(prev, current)
            return head

        head = recursion(None, head)
        return head
