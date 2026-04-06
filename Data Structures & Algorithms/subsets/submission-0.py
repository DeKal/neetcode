class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        pos = [None]*(len(nums))



        def gen_subset(pos, cur, l, r):
            nonlocal result

            if cur > r: 
                return
            
            res = []
            for i in range(0, cur):
                if pos[i] is not None:
                    res.append(nums[pos[i]])
            result.append(res)

            for i in range(l, r):
                pos[cur] = i
                gen_subset(pos, cur+1, i+1, r)
                

        gen_subset(pos, 0, 0, len(nums))

        return result