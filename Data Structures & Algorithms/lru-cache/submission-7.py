class Node:
    def __init__(self, key=0, value=0, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map_dict = {} # {key:node}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def _add(self, node):
        temp = self.head.next
        self.head.next = node
        node.next = temp
        temp.prev = node
        node.prev = self.head

    def get(self, key: int) -> int:
        node = self.map_dict.get(key)
        if not node:
            return -1
        self._remove(node)
        self._add(node)
        return node.value


    def put(self, key: int, value: int) -> None:
        # check if update
        node = self.map_dict.get(key)
        if node:
            node.value = value
            self._remove(node)
            self._add(node)
        else:
            # check capacity
            if len(self.map_dict)==self.capacity:
                old_node = self.tail.prev
                self.map_dict.pop(old_node.key)
                self._remove(old_node)
            # insert
            node = Node(key=key, value=value)
            self.map_dict[key] = node
            self._add(node)
        
