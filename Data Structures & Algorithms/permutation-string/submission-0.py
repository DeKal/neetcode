class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}

        for ch in s1:
            s1_dict[ch] = s1_dict.get(ch,0) + 1

        n = len(s2)
        
        l = 0
        cur_dict = {}
        for i in range(0, n):
            if s2[i] in s1_dict:
                cur_dict[s2[i]] = cur_dict.get(s2[i],0)+1

                if cur_dict == s1_dict:
                    return True
                elif i-l+1 == len(s1):
                    
                    cur_dict[s2[l]] -= 1
                    l += 1


            else:
                # reset if see different char
                cur_dict = {}
                # move l to the next position (maybe in the s1 dict)
                l = i+1



        return False