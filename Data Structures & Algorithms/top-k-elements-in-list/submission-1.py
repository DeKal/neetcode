

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = {}

        for i in range(0,n):
            num = nums[i]
            freq[num] = freq.get(num, 0) + 1
        
        # h = []
        # heapq.heapify(h)
        
        # for item in freq.items():
        #     heapq.heappush(h, (item[1], item))
        #     if len(h) > k:
        #         heapq.heappop(h)

        # result = []
        # for el in h:
        #     item = el[1]
        #     key = item[0]
        #     result.append(key)
        
        freqArr = [[] for i in range(len(nums)+1)]

        for num, freqNum in freq.items():
            freqArr[freqNum].append(num)


        res = []
        for i in range(len(freqArr) - 1, 0, -1):
            for num in freqArr[i]:
                res.append(num)
                if len(res) == k:
                    return res


        return res