class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 5 6 1 2 3 4
        # 3 4 5 6 1 2
        n = len(nums)
        l = 0
        r = n-1
        # 

        while l<=r:
            m = l + (r-l)//2
     
            if target == nums[m]:
                return m
            if nums[l] <= nums[m]: # left half
                if nums[l] <= target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            else: # right half
                if nums[m] < target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
        
        return -1