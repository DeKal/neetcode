class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        print(count)

        max_heap =[-cnt for cnt in count.values()]
        heapq.heapify(max_heap)
        
        cool_down_queue = deque([])  # pairs of [-cnt, idleTime]

        time = 0
        while max_heap or cool_down_queue:
            time += 1
            if not max_heap:
                time = cool_down_queue[0][1] # idle time of the queue
            else:
                cnt = 1 + heapq.heappop(max_heap) # pop item from max heap with count
                if cnt<0:
                    cool_down_queue.append([cnt, time+n])
            
            if cool_down_queue and cool_down_queue[0][1] <= time:
                cnt, t = cool_down_queue.popleft()
                heapq.heappush(max_heap, cnt)
        

        return time
        
            
            

