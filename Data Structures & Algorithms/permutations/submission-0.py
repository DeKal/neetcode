class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        results = []
        pos = [0]*(n)
        nums_set = set()
        def gen_permutation(nums_set, pos, cur_pos):
        

            if cur_pos == n:
                results.append(pos.copy())
                return
            
            for i in range(0, n):
                if nums[i] not in nums_set:
                    pos[cur_pos] = nums[i]
                    nums_set.add(nums[i])
                    gen_permutation(nums_set, pos, cur_pos+1)
                    nums_set.remove(nums[i])
                
        gen_permutation(nums_set, pos, 0)
        return results
