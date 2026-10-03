# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur_1, cur_2, cur_new = l1, l2, dummy
        carry = 0
        while cur_1 or cur_2:
            cur_1_val = cur_1.val if (cur_1 and cur_1.val) else 0
            cur_2_val = cur_2.val if (cur_2 and cur_2.val) else 0
            new_sum = cur_1_val+cur_2_val+carry
            cur_new.next = ListNode(val=new_sum%10)
            carry = new_sum//10
            if cur_1:
                cur_1 = cur_1.next
            if cur_2:
                cur_2 = cur_2.next
            cur_new = cur_new.next
        if carry:
            cur_new.next = ListNode(val=carry)
        return dummy.next
            

        