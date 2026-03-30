class Solution:

    def toOccurenceTuple(self, s: str):
        occurrences = [0]*26
        for c in s:
           occurrences[ord(c)-ord('a')] +=1
        return tuple(occurrences)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dt = dict()

        for s in strs:
            s_occurrence = self.toOccurenceTuple(s)
            if s_occurrence not in dt:
                dt[s_occurrence] = []
            dt[s_occurrence].append(s)
        print(dt)
        return list(dt.values())


