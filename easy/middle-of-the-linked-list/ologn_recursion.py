class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"Node value is: {self.val}"


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        num = self.numbers_of_nodes(head) // 2
        for i in range(num):
            head = head.next
        return head

    def numbers_of_nodes(self, head: ListNode, nodes=1) -> int:
        if head.next:
            nodes = self.numbers_of_nodes(head.next, nodes + 1)
        return nodes


sol = Solution()

llist6 = ListNode(6)
llist5 = ListNode(5, next=llist6)
llist4 = ListNode(4, next=llist5)
llist3 = ListNode(3, next=llist4)
llist2 = ListNode(2, next=llist3)
llist = ListNode(1, next=llist2)
print("Among 6 nodes:", sol.middleNode(llist))

llist5 = ListNode(5)
llist4 = ListNode(4, next=llist5)
llist3 = ListNode(3, next=llist4)
llist2 = ListNode(2, next=llist3)
llist = ListNode(1, next=llist2)
print("Among 5 nodes:", sol.middleNode(llist))

llist4 = ListNode(4)
llist3 = ListNode(3, next=llist4)
llist2 = ListNode(2, next=llist3)
llist = ListNode(1, next=llist2)
print("Among 4 nodes:", sol.middleNode(llist))

llist3 = ListNode(3)
llist2 = ListNode(2, next=llist3)
llist = ListNode(1, next=llist2)
print("Among 3 nodes:", sol.middleNode(llist))

llist2 = ListNode(2)
llist = ListNode(1, next=llist2)
print("Among 2 nodes:", sol.middleNode(llist))

llist = ListNode(1)
print("Among 1 nodes:", sol.middleNode(llist))
