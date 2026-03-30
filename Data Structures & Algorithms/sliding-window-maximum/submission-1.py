class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        heapq.heapify(h)


        for i in range(0, k):
            heapq.heappush(h, (-nums[i],i))

        n = len(nums)
        window_size = 0
        res = [-h[0][0]]
        for i in range(k, n):
            heapq.heappush(h, (-nums[i],i))
            most_left = nums[i-k]

            top = h[0]
            # if -top[0] == most_left and top[1] == i-k:
            #     heapq.heappop(h)
            # else:
            while top[1] <= i-k:
                heapq.heappop(h)
                top = h[0]
            res.append(-top[0])

        print(res)
            

        return res

        