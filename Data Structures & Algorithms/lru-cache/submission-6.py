class Node:
    def __init__(self, key: int, val:int, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_node = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        temp_next = node.next
        temp_prev = node.prev
        node.next.prev = temp_prev
        node.prev.next = temp_next
        del node

    def _add(self, node):
        temp = self.head.next
        self.head.next = node
        node.next = temp
        temp.prev = node
        node.prev = self.head
        

    def get(self, key: int) -> int:
        node = self.key_node.get(key)
        if not node:
            return -1
        else:
            self._remove(node)
            self._add(node)
            return node.val
        

    def put(self, key: int, value: int) -> None:
        node = self.key_node.get(key)
        if node:
            node.val = value
            self._remove(node)
            self._add(node)
        else:
            if len(self.key_node)>=self.capacity:
                old = self.tail.prev
                self.key_node.pop(old.key)
                self._remove(old)
            node = Node(key, value)
            self.key_node[key] = node
            self._add(node)

        
