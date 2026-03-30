# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        extra = 0
        cur1 = l1
        cur2 = l2


        while cur2:
        
            s = cur1.val + cur2.val + extra
            extra = s//10
            cur1.val = s%10 
            
            if cur1.next == None:
                if cur2.next is not None:
                    cur1.next = ListNode()
                elif extra:
                    cur1.next = ListNode(1, None)
            elif cur2.next == None:
                cur2.next = ListNode()
            cur1 = cur1.next
            cur2 = cur2.next


        return l1
