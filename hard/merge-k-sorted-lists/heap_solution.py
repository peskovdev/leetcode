from typing import Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        minheap = []
        for node in lists:
            if node:
                minheap.append((node.val, id(node), node))
        heapq.heapify(minheap)
        while minheap:
            _, _, node = heapq.heappop(minheap)
            cur.next, cur = node, node
            if node.next:
                node = node.next
                heapq.heappush(minheap, (node.val, id(node), node))
        return dummy.next
