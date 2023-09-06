from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> list[Optional[ListNode]]:
        list_len = self.get_len(head)
        nodes_number = list_len // k
        extras = list_len % k

        store: list[Optional[ListNode]] = []
        for i in range(k):
            if head is not None:
                store.append(head)
                for _ in range(nodes_number - 1 + (1 if extras else 0)):
                    head = head.next
                if extras:
                    extras -= 1
                head.next, head = None, head.next
            else:
                store.append(None)
        return store

    def get_len(self, head: Optional[ListNode]) -> int:
        if head is None:
            return 0
        return 1 + self.get_len(head.next)
