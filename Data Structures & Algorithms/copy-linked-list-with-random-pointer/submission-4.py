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
        # think about None situation
        # create new node as the next of the old one
        cur = head
        while cur:
            new_node = Node(cur.val, next=cur.next)
            cur.next = new_node
            cur = new_node.next
        # link the random on the new one, consider None situation
        cur = head
        while cur:
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next
        # seperate the old list and new list
        dummy = Node(0)
        cur = head
        new_cur = dummy
        while cur:
           new_cur.next = cur.next
           new_cur = new_cur.next
           cur.next = new_cur.next
           cur = cur.next
        return dummy.next 


        