from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.left = head

        def recurse(right: Optional[ListNode]):
            if right is None:
                return
            if recurse(right.next) is False:
                return False

            left, self.left = self.left, self.left.next
            return left.val == right.val

        return recurse(head)
