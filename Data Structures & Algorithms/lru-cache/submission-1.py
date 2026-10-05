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


    def get(self, key: int) -> int:
        if self.node_map.get(key):
            node = self.node_map.get(key)
            node.prev.nxt = node.nxt
            node.nxt.prev = node.prev
            node.nxt = self.tail_dummy
            node.prev = self.tail_dummy.prev
            self.tail_dummy.prev.nxt = node
            self.tail_dummy.prev = node
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        node = self.node_map.get(key)
        if node:
            node.val = value
            node.prev.nxt = node.nxt
            node.nxt.prev = node.prev
            node.prev = self.tail_dummy.prev
            node.nxt = self.tail_dummy
        else:
            cache_len = len(self.node_map)
            if cache_len>=self.capacity:
                self.node_map.pop(self.head_dummy.nxt.key)
                least_node = self.head_dummy.nxt
                self.head_dummy.nxt = least_node.nxt
                least_node.nxt.prev = self.head_dummy
            node = Node(val=value, prev=self.tail_dummy.prev, nxt=self.tail_dummy, key=key)
            self.node_map[key] = node
        # update tail
        self.tail_dummy.prev.nxt = node
        self.tail_dummy.prev = node

        
        


