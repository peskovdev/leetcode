from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True

        # find the middle by position of slow pointer
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse linked list from end to midle
        cur, prev = slow, None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # check values
        left, middle, right = head, slow, prev
        while (left or right) is not middle:
            if left.val != right.val:
                return False
            left, right = left.next, right.next
        return True
