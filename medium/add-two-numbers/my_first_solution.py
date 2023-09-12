from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> Optional[ListNode]:
        num1 = self.get_num(l1)
        num2 = self.get_num(l2)
        if num1 + num2 == 0:
            return ListNode(val=0, next=None)

        def create_list(num: int):
            if num == 0:
                return None

            node = ListNode(val=num % 10)
            nxt = create_list(num // 10)
            node.next = nxt
            return node

        return create_list(num1 + num2)

    def get_num(self, head: ListNode) -> int:
        if head.next is None:
            return head.val
        num = self.get_num(head.next)
        return num * 10 + head.val
