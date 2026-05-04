class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = cur_sum = 0

        prefix_sums = {}
        prefix_sums[0] = 1

        
        for num in nums:
            cur_sum += num
            diff = cur_sum - k
            res += prefix_sums.get(diff, 0)
            prefix_sums[cur_sum] = prefix_sums.get(cur_sum,0)+1


        return res