class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        results = []
        result = []
        def gen_sum(result, l, cur_sum):

            nonlocal results

            if cur_sum == target:

                results.append(result.copy())
                return

            for i in range(l, len(nums)):
                num = nums[i]
                if cur_sum + num <= target:
                    result.append(num)
                    gen_sum(result, i, cur_sum + num)
                    result.pop()

        gen_sum(result, 0, 0)
        return results