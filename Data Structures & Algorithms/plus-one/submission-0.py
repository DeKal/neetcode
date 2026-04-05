class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        digits[-1] += 1 
        carrier = 0
        for i in reversed(range(0, n)):
            sum = digits[i] + carrier
            digits[i] = sum % 10
            carrier = sum // 10

        if carrier:
            res = [1]
            for digit in digits:
                res.append(digit)
            return res
        return digits

