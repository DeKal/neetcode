class Solution:
    def area(self, lh, rh, width):
        return min(lh, rh) * width

    def maxArea(self, a: List[int]) -> int:
        n = len(a)
        l = 0
        r = n-1
        maxArea = 0
        while l<r:
            maxArea = max(maxArea, self.area(a[l], a[r], r-l))
   
            if a[l] <= a[r]:
                l+=1
            elif a[l] > a[r]:
                r-=1

        return maxArea