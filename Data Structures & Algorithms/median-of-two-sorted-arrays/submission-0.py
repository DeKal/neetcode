class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 1 2 3 4 5 6 
        # 3 5 5 6 7 8
        #        L M R          

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        l = 0
        r = len(nums1) - 1
        total = len(nums1) + len(nums2)
        half = total // 2
        
        while True:
            num1_mid_pos = l + (r-l)//2
            num2_mid_pos = half - num1_mid_pos - 2

            num1_mid = nums1[num1_mid_pos] if num1_mid_pos >=0 else -math.inf
            num2_mid = nums2[num2_mid_pos] if num2_mid_pos >=0 else -math.inf
            num1_mid_nxt = nums1[num1_mid_pos+1] if num1_mid_pos+1<len(nums1) else math.inf
            num2_mid_nxt = nums2[num2_mid_pos+1] if  num2_mid_pos+1<len(nums2) else math.inf

            if num1_mid <= num2_mid_nxt and num2_mid <= num1_mid_nxt:
                if total%2 == 0:
                    return (max(num1_mid, num2_mid) + min(num1_mid_nxt, num2_mid_nxt)) /2
                else:
                    return min(num1_mid_nxt, num2_mid_nxt)
            elif num1_mid > num2_mid_nxt:
                r = num1_mid_pos - 1
            else:
                l = num1_mid_pos +1


        return -1


        