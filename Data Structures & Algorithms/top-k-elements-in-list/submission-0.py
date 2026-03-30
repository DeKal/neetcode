

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = {}

        for i in range(0,n):
            num = nums[i]
            freq[num] = freq.get(num, 0) + 1
        
        h = []
        heapq.heapify(h)
        
        for item in freq.items():
            heapq.heappush(h, (item[1], item))
            if len(h) > k:
                heapq.heappop(h)
        
        print(h)

        result = []
        for el in h:
            item = el[1]
            key = item[0]
            result.append(key)

        return result