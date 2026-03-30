# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()

        cur_head1 = list1
        cur_head2 = list2
        cur_insert = new_head
    
        while cur_head1 or cur_head2:
            if not cur_head2 or cur_head1 and cur_head1.val <= cur_head2.val:
                cur_insert.next = cur_head1
                cur_head1 = cur_head1.next
            elif not cur_head1 or cur_head2 and cur_head1.val > cur_head2.val:
                cur_insert.next = cur_head2
                cur_head2 = cur_head2.next
            
            cur_insert = cur_insert.next

        return new_head.next