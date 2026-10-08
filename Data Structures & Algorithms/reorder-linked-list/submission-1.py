# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeList(self, node1, node2):
        dummy = ListNode()
        cur = dummy
        while node1 or node2:
            cur.next = node1
            temp1=node1.next if node1 else None
            node1.next = node2
            temp2 = node2.next if node2 else None
            cur = node2
            node1 = temp1
            node2 = temp2
        return dummy.next

    def reverseList(self, node):
        prev, cur = None, node
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev


    def reorderList(self, head: Optional[ListNode]) -> None:
        # use slow and fast to find out the middle 
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        temp = slow.next
        slow.next = None
        # reverse right part
        reversed_list = self.reverseList(temp)
        # link left part and reversed right part
        reordered_list = self.mergeList(head, reversed_list)

        