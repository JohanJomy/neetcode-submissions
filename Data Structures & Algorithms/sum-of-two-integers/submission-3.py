class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = 0xFFFFFFFF # 11111111111...11 (32)
        max_int = 0x7FFFFFFF 
        
        res = (a ^ b) & mask 
        carry = ((a & b) << 1)&mask
        
        while carry:
            t = (res & carry) << 1
            res = (res ^ carry) & mask
            carry = t & mask
        
        return res if res <= max_int else ~ (res ^ mask)

