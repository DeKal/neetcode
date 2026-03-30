class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        # for l in range(0, n-1):
        #     r = l+1
        #     while r<n and numbers[l] + numbers[r] < target:
        #         r += 1
        #     if r<n and numbers[l] + numbers[r] == target:
        #         return[l+1, r+1]
        
        l = 0
        r = n-1

        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1, r+1]

        

        return [-1, -1]