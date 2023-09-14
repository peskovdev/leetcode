class ListNode:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: dict[int, ListNode] = {}
        self.dummy = ListNode()
        self.mru = self.dummy

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.refresh_cache(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.refresh_cache(self.cache[key])
        else:
            node = ListNode(key=key, val=value)
            self.insert(node)
            self.cache[key] = node
            if len(self.cache) > self.capacity:
                lru = self.pop_node(self.dummy.next)
                del self.cache[lru.key]
                del lru

    def refresh_cache(self, node):
        if node.next is not None:
            self.pop_node(node)
            self.insert(node)

    def pop_node(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        return node

    def insert(self, node):
        self.mru.next = node
        node.prev = self.mru
        node.next = None
        self.mru = node
