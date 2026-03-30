# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        k = len(lists)
        if k == 0:
            return 
        
        
        current_heap = []
        heapq.heapify(current_heap)
        res = ListNode()
        cur_res = res

        curs = [lists[i] for i in range(0,k)] 
        count = 0
        for i in range(0,k):
            cur = curs[i]
            if curs[i]:
                heapq.heappush(current_heap, (cur.val, count, cur))
                count += 1
        
        while current_heap:
        
            val, count, node = heapq.heappop(current_heap)
            next_node = node.next
            if next_node:
                heapq.heappush(current_heap, (next_node.val, count, next_node))
                count += 1

            cur_res.next = node
            cur_res = cur_res.next

            

        return res.next


        