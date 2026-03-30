class Solution:

    def isMaxKChanges(self, occ: dict, k:int) -> bool:
        if not occ:
            return False
        all_times = 0
        max_time_pos = 'A'
        max_times = 0
        for key, times in occ.items():
            all_times += times
            if max_times < times:
                max_times = times
                max_time_pos = key
        return all_times - occ[max_time_pos] > k
        

    def characterReplacement(self, s: str, k: int) -> int:
        l = max_length = 0

        n = len(s)
        c_occ = {}
        diff = 0
        for r in range(0, n):
            c_occ[s[r]] = c_occ.get(s[r], 0) + 1
            while self.isMaxKChanges(c_occ, k):
    
                c_occ[s[l]] = c_occ[s[l]] - 1
                l+=1

           
                
            max_length = max(max_length, r-l+1)


        return max_length