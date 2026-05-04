class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        n = len(nums)
        l = 0
        cur_sum = 0
        res = n
        for r in range(n):
            cur_sum += nums[r]
            while cur_sum>=target:
                res = min(r - l + 1, res)
                cur_sum-=nums[l]
                l+=1
               
    
            
            
           


        return res
