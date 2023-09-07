from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        zero_head = ListNode(val=0, next=head)
        cur = zero_head
        for _ in range(left - 1):
            cur = cur.next
        cur.next = self.reverse_linked_list(cur.next, right - left + 1)
        return zero_head.next

    def reverse_linked_list(self, head: Optional[ListNode], reversed_node_numbers: int):
        prev = None
        cur = head
        for _ in range(reversed_node_numbers):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        head.next = cur
        return prev
