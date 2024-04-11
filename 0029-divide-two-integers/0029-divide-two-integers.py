class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend > 0) == (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not sign:
            res = -res

        return min(max(-2**31, res), 2**31 - 1)