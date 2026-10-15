# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse_list(head):
            prev, cur = None, head
            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev

        def interleave_lists(head1, head2):
            cur1, cur2 = head1, head2
            while cur1 and cur2:
                temp1 = cur1.next
                cur1.next = cur2
                cur1 = temp1
                temp2 = cur2.next
                if cur1:
                    cur2.next = cur1
                cur2 = temp2

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head_1 = slow.next
        slow.next = None
        new_head_1 = reverse_list(head_1)
        interleave_lists(head, new_head_1)