class Solution:
    def findMin(self, nums: List[int]) -> int:
        # l   m   r 

        #  1 2 3 4 5 6 7
        #. 6 7 1 2 3 4 5
        #. 3 4 5 6 7 1 2

        n = len(nums)
        l = 0
        r = n-1

        while l<r:
            m = l + (r-l)//2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m+1
        return nums[r]
