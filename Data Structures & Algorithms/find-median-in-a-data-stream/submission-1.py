class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []        

    def addNum(self, num: int) -> None:

        if not self.min_heap:
            heapq.heappush(self.min_heap, num)
            return

        if self.min_heap[0] <= num:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)

        if len(self.min_heap) > len(self.max_heap)+1:
            min_val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_val)
        elif len(self.max_heap) > len(self.min_heap)+1:
            max_val = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -max_val)

        print("+++++")
        print(self.min_heap)
        print(self.max_heap)
        
        
        

    def findMedian(self) -> float:
        if len(self.min_heap)== len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0])/2
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return -self.max_heap[0]
            