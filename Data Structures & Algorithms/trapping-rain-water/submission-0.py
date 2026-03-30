class Solution:
    
    def trap(self, a: List[int]) -> int:
        n = len(a)
       
        area = 0

        l = 0
        r = n-1

        leftHeightMax = a[l]
        rightHeightMax = a[r]

        while l<r:
            if leftHeightMax < rightHeightMax:
                l += 1
                leftHeightMax = max(leftHeightMax, a[l])
                area += (leftHeightMax-a[l])
            else:
                r -= 1
                rightHeightMax = max(rightHeightMax, a[r])
                area += (rightHeightMax-a[r])

        return area
