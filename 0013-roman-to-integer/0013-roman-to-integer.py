class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        prev = 0
        for char in s :
                val = roman_map[char]
                if val > prev:
                        result += val - 2*prev
                else:
                        result += val
                prev = val
        return result
                