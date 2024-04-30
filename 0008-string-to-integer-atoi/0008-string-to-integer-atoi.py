class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        index = 0
        while index < len(s) and s[index].isdigit():
            index += 1
        s = s[:index]
        if not s:
            return 0
        result = int(s)
        result *= sign
        return result if -2**31 <= result <= 2**31 - 1 else -2**31 if result < 0 else 2**31 - 1