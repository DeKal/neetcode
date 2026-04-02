class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        heapq.heapify(max_heap)

        for stone in stones:
            heapq.heappush(max_heap, -stone)

        while len(max_heap)>1:
            max_stone = -heapq.heappop(max_heap)
            next_max_stone = -heapq.heappop(max_heap)
            heapq.heappush(max_heap, -abs(next_max_stone - max_stone))

        return -max_heap[0]