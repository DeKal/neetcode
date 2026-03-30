class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # position 
        n = len(heights)
        max_area = 0

        #[7,1,7,2,2,1,4]

        # 1 2  
        for i in range(0,n+1):
    
            while stack and (i==n or heights[i] <= heights[stack[-1]]):
                current_top_pos = stack.pop()
          
                width = i-stack[-1]-1 if stack else i
                
                area = heights[current_top_pos]*width
                max_area = max(max_area, area)
                
                
            stack.append(i)

        return max_area