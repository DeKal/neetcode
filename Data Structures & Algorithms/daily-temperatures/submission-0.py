class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack = deque([0])
        for i in range(1, n):
            temperature = temperatures[i]
            while stack and temperatures[stack[-1]] < temperature:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            
            stack.append(i)
        
        return res
                