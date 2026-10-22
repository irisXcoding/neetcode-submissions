class Node:
    def __init__(self, val: int, key: int, prev=None, nxt=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.nxt = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.head =  Node(0, 0)
        self.tail =  Node(0, 0)
        self.head.nxt = self.tail
        self.tail.prev = self.head
        self.key_node_map = {}
        self.capacity = capacity
    
    def _remove_node(self, node):
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev
        node.nxt, node.prev = None, None # clear cache

    def _insert_node(self, node, prev_node):
        temp = prev_node.nxt
        prev_node.nxt = node
        node.nxt = temp
        temp.prev = node
        node.prev = prev_node

    def get(self, key: int) -> int:
        node = self.key_node_map.get(key)
        if not node:
            return -1
        self._remove_node(node)
        self._insert_node(node, self.head)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.key_node_map.get(key)
        if not node:
            if len(self.key_node_map)>=self.capacity:
                oldest = self.tail.prev
                self._remove_node(oldest)
                self.key_node_map.pop(oldest.key)
            node = Node(value, key)
            self.key_node_map[key] = node
            self._insert_node(node, self.head)
        else:
            node.val = value
            self._remove_node(node)
            self._insert_node(node, self.head)
        
