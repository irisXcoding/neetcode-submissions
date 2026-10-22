from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def _merge_list(self, node1, node2):
        dummy = ListNode()
        cur = dummy
        while node1 and node2:
            if node1.val < node2.val:
                cur.next = node1
                node1 = node1.next
            else:
                cur.next = node2
                node2 = node2.next
            cur = cur.next
        if node1:
            cur.next = node1
        if node2:
            cur.next = node2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [item for item in lists if item]
        if not lists:
            return None
        dq = deque(lists)
        while len(dq)>1:
            node1 = dq.popleft()
            node2 = dq.popleft()
            merged_list = self._merge_list(node1, node2)
            dq.append(merged_list)
        return dq[0]


        