class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
     


        #[0,3,2,5,4,6,1,1] 
        # Set 0 3 2 5 4 
        # Left most of
        # 3->2 4->2 5->2
        # Right most of
        # 2->6 
        num_set = set(nums)
        res = 0
        for num in num_set:
            if num-1 not in num_set:
                next_num = num + 1
                while next_num in num_set:
                    next_num += 1
                res = max(res, next_num - num)
                

        return res