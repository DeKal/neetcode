class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if n < 2:
            return nums
        
        left_products = [1]*n
        right_products = [1]*n

        left_products[0] = nums[0]
        for i in range(1, n):
            left_products[i] = left_products[i-1] * nums[i]

        right_products[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            right_products[i] = right_products[i+1] * nums[i]

        nums[0] = right_products[1]
        nums[-1] = left_products[n-2]
        for i in range(1, n-1):
            nums[i] = left_products[i-1] * right_products[i+1]
       

        return nums