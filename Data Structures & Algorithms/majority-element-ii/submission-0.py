class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        expected_count = n//3

        num1 = -1
        num2 = -1
        count1 = 0
        count2 = 0

        for num in nums:
            if num == num1:
                count1 += 1
            elif num == num2:
                count2 += 1
            elif count1 == 0:
                count1 = 1
                num1 = num
            elif count2 == 0:
                count2 = 1
                num2 = num
            else:
                count2 -= 1
                count1 -= 1


        count1 = 0
        count2 = 0
        for num in nums:
            if num == num1:
                count1 += 1
            elif num == num2:
                count2 += 1

        res = []
        if count1 > expected_count:
            res.append(num1)
        if count2 > expected_count:
            res.append(num2)
        return res