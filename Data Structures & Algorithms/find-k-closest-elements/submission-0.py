class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k
        
        while l <= r:
            m = (l + r) // 2
            
            # Compare: Should we shift window right?
            # Distance from x to left edge vs distance from x to right edge (outside current window)
            if m + k < len(arr) and x - arr[m] > arr[m + k] - x:
                l = m + 1  # Window should be more to the right
            else:
                r = m - 1  # Window should be at or left of m
        
        # After loop: l is the leftmost valid starting position
        return arr[l:l + k]