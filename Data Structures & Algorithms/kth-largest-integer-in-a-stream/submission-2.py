class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.max_heap = []
        self.min_heap = []
        self.k = k
        heapq.heapify(self.max_heap)
        heapq.heapify(self.min_heap)

        for num in nums: 
            heapq.heappush(self.max_heap, -num)

        for i in range(0,k):
            if self.max_heap:
                max_num = -heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, max_num)



    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, val)

        return self.min_heap[0]
        
