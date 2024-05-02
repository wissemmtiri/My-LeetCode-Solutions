class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = {}
        max_length = -1
        for i, c in enumerate(s):
            if c in seen:
                max_length = max(max_length, i - seen[c] - 1)
            else:
                seen[c] = i
        return max_length