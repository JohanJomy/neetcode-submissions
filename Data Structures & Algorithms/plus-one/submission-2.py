class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1

        num = digits[i] + 1
        carry = num // 10
        rem = num % 10

        while carry and i > 0:
            digits[i] = rem

            i -= 1
            num = digits[i] + 1
            carry = num // 10
            rem = num % 10

        digits[i] = rem

        if carry:
            return [carry] + digits
        
        return digits


