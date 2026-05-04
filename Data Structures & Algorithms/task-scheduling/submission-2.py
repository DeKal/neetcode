class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
 

        max_heap =[-cnt for cnt in count.values()]
        heapq.heapify(max_heap)
        
        cool_down_queue = deque([])  # pairs of [-cnt, idleTime]

        time = 0
        while max_heap or cool_down_queue:
            time += 1 
            if not max_heap:
                time = cool_down_queue[0][1] # if heap empty the get item from cool_down_queue
            else:
                count = 1 + heapq.heappop(max_heap) # decrease count 
                if count<0: # still have work
                    cool_down_queue.append([count, time+n])
            
            if cool_down_queue and cool_down_queue[0][1] <= time:
                heapq.heappush(max_heap, cool_down_queue.popleft()[0])


        return time
        
            
            

