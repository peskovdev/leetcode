from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        def recurse_and_remove(head: Optional[ListNode]):
            if head is None:
                return 0, None

            depth, nxt = recurse_and_remove(head.next)
            current_depth = depth + 1
            head.next = nxt

            if current_depth == n:
                head = nxt

            return current_depth, head

        recurse_and_remove(dummy)
        return dummy.next
