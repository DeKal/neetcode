class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current_max_pos = 0

        for i in range(len(nums)):
            num = nums[i]

            if current_max_pos >= i:
                current_max_pos = max(current_max_pos, i + num)
                print(current_max_pos)

        return current_max_pos >= len(nums)-1

