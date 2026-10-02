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
        # pass 1
        cur = head
        old_to_new = {}
        while cur:
            new_cur = Node(cur.val)
            old_to_new[cur] = new_cur
            cur = cur.next
        # pass 2
        dummy = Node(0)
        cur = head
        if cur and old_to_new[cur]:
            dummy.next = old_to_new[cur]
        while cur:
            new_cur = old_to_new[cur]
            cur_next = cur.next
            cur_random = cur.random
            if cur_next:
                new_cur_next = old_to_new[cur_next]
                new_cur.next = new_cur_next
            if cur_random:
                new_cur_random = old_to_new[cur_random]
                new_cur.random = new_cur_random
            cur = cur.next
        return dummy.next
