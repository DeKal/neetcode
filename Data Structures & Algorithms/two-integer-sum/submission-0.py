class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        result = []
        dct = {}

        for i in range(0,n): 
            num = nums[i]
            counter_part = target - num

            if counter_part in dct:
                return [dct[counter_part], i]

            if num not in dct:
                dct[num] = i
            
        return result
