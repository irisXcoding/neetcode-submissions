class Node:
    def __init__(self, val=-1, prev=-1, nxt=-1, key=-1):
        self.val = val
        self.prev = prev
        self.nxt = nxt
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.head_dummy = Node()
        self.tail_dummy = Node()
        self.head_dummy.nxt = self.tail_dummy
        self.tail_dummy.prev = self.head_dummy
        self.node_map = {}
        self.capacity = capacity

    def _insert(self, node):
        node.nxt = self.tail_dummy
        node.prev = self.tail_dummy.prev
        self.tail_dummy.prev.nxt = node
        self.tail_dummy.prev = node

    def _delete(self, node):
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev


    def get(self, key: int) -> int:
        if self.node_map.get(key):
            node = self.node_map.get(key)
            self._delete(node)
            self._insert(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if self.node_map.get(key):
            node = self.node_map.get(key)
            node.val = value
            self._delete(node)
        else:
            cache_len = len(self.node_map)
            if cache_len>=self.capacity:
                self.node_map.pop(self.head_dummy.nxt.key)
                self._delete(self.head_dummy.nxt)
            node = Node(val=value, key=key)
            self.node_map[key] = node
        self._insert(node)
