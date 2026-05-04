class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda t: t[0])


        res = []
        min_heap = []
        i = 0
        time = tasks[0][0]

        while min_heap or i < len(tasks):
            # try to execute tasks if the time is match with enqueueing time
            while i<len(tasks) and time >= tasks[i][0]:
                # push to heap processing time, task count for prioritizing
                heapq.heappush(min_heap, [tasks[i][1], tasks[i][2]])
                i += 1
            
            if not min_heap: # no item wait to be processing
                time = tasks[i][0] # increase time to match
            else:
                processing_time, count = heapq.heappop(min_heap)
                time += processing_time
                res.append(count)

        return res



