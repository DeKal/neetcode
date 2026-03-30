class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        
        for c in s:
            if q:
                top_stack = q[-1]
                if c == "}" and top_stack == "{" or c == ")" and top_stack == "(" or c == "]" and top_stack == "[":
                    q.pop()
                else:
                    q.append(c)
            else:
                q.append(c)
    
        return not len(q)
            