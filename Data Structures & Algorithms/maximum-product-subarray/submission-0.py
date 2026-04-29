class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cur_max, cur_min = 1, 1

        for num in nums:
            tmp = cur_max * num
            cur_max = max(cur_max * num, cur_min * num, num)
            cur_min = min(tmp, cur_min * num, num)

            res = max(cur_max, res)

        return res