from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:  # only for empty initial node
            return head

        new_head = head  # will be set on last recursion lvl
        if head.next:
            new_head = self.reverseList(head.next)  # just will represent new head of linked list, no more
            head.next.next = head
        head.next = None
        # 1) set node.next to None
        # 2) set prev.node.next to prev
        # 3) set prev.next to None
        # 4) again

        return new_head  # returned head
