# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # find the start of the reversed linked list
        reverse_head = slow.next
        slow.next = None
        prev, cur = None, reverse_head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        cur_1, cur_2 = head, prev
        # merge head and left
        while cur_1 and cur_2:
            temp_1 = cur_1.next
            temp_2 = cur_2.next
            cur_1.next = cur_2
            cur_2.next = temp_1
            cur_1 = temp_1
            cur_2 = temp_2
