class Solution:
    def longestPalindrome(self, s: str) -> str:
        chf = ''
        for i in range(len(s)):  # Start iterating from i = 0
            for j in range(len(s) - 1, i - 1, -1):  # Also consider j = i
                tr = s[i:j + 1]
                if tr == tr[::-1] and len(tr) > len(chf):
                    chf = tr
        return chf