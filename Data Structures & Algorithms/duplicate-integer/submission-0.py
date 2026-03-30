class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)

        setNum = set()

        for i in range(0, n):
            if nums[i] not in setNum:
                setNum.add(nums[i])
            else:
                return True


        return False