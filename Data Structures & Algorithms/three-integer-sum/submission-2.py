class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        nums.sort() # O(nlogn)

        result = set()
        for target_pos in range(0, n-2):
            target = -nums[target_pos]
            l = target_pos+1
            r = n-1
            while l<r:
                if nums[l] + nums[r] == target:
                    result.add(tuple([-target, nums[l], nums[r]]))
                    l+=1
                    r-=1
                elif nums[l] + nums[r]> target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
        
        return [list(res) for res in result]


