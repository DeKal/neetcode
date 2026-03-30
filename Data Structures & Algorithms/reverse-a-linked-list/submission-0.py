# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        new_head = ListNode()

        cur = head
        while cur:
            next_head = new_head.next
            new_head.next = cur

            next_cur = cur.next
            cur.next = next_head
        
            cur = next_cur
        
        return new_head.next