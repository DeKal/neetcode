class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 0:
            return nums

        n = len(nums)

        result = [0]*2*n
        for i in range(0, n*2):
            result[i] = nums[i%n]

        print(result)

        return result