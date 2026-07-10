from collections import deque

class LinkNode:

    def __init__(self, key=None, val=None, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.kv_store = {}
        self.capacity = capacity

        self.head = LinkNode()
        self.tail = LinkNode()
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev

    def _add_front(self, node):
        node.prev = self.head
        node.nxt = self.head.nxt
        self.head.nxt.prev = node
        self.head.nxt = node

    def get(self, key: int) -> int:
        if key not in self.kv_store:
            return -1

        node = self.kv_store[key]

        self._remove(node)
        self._add_front(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.kv_store:
            node = self.kv_store[key]
            node.val = value
            self._remove(node)
            self._add_front(node)
            return

        if len(self.kv_store.keys()) >= self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.kv_store[lru.key]

        node = LinkNode(key=key, val=value)
        self.kv_store[key] = node
        self._add_front(node)
        
        