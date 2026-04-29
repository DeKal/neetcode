class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        nums.append(0)
        n = len(nums)
      
        cost = [0]*n
        cost[0] = nums[0]
        cost[1] = max(nums[0], nums[1])

        for i in range(2, n):
            cost[i] = max(cost[i-2]+nums[i], cost[i-1])

        return cost[-1]