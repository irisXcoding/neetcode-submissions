# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def _merge(self, head1, head2):
        if not head2:
            return head1 
        if not head1:
            return head2 
        dummy = ListNode()
        cur = dummy
        while head1 and head2:
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        if head1:
            cur.next = head1
        if head2:
            cur.next = head2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        while len(lists)>1:
            slow = 0
            new_lists = []
            while slow<=len(lists)-1:
                if slow == len(lists)-1:
                    new_linked_list = self._merge(lists[slow], None)
                else:    
                    new_linked_list = self._merge(lists[slow], lists[slow+1])
                new_lists.append(new_linked_list)
                slow+=2
            lists = new_lists
        return lists[0]
            
        