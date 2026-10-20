# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(node):
            prev, cur = None, node
            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur =temp
            return prev

        def interleave(node1, node2):
            while node1 and node2:
                temp1 = node1.next
                node1.next = node2
                temp2 = node2.next
                if temp1:
                    node2.next = temp1
                node1 = temp1
                node2 = temp2


        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        reversed_list = reverse(slow.next)
        slow.next = None
        interleave(head, reversed_list)