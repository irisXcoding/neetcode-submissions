"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # create the new linked list and node_map
        cur = head
        node_map = {None:None}
        while cur:
            new_node = Node(x=cur.val)
            node_map[cur] = new_node
            cur = cur.next
        # link the items in new linked list
        dummy = Node(0)
        dummy.next = node_map[head]
        cur = head
        while cur:
            new_cur = node_map[cur]
            new_cur.next = node_map[cur.next]
            new_cur.random = node_map[cur.random]
            cur = cur.next
        return dummy.next

        