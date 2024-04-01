class Solution:
    def longestPalindrome(self, s: str) -> str:
        strLen = 2 * len(s) + 3
        sChars = [0]*strLen

        sChars[0] = '@'
        sChars[strLen - 1] = '$'
        t = 1
        for i in s:
            sChars[t] = '#'
            t += 1
            sChars[t] = i
            t += 1

        sChars[t] = '#'

        maxLen = int(0)
        start = int(0)
        maxRight = int(0)
        center = int(0)
        p = [0] * strLen  
        for i in range(1, strLen - 1):
            if i < maxRight:
                p[i] = min(maxRight - i, p[2 * center - i])

            while sChars[i + p[i] + 1] == sChars[i - p[i] - 1]:
                p[i] += 1

            if i + p[i] > maxRight:
                center = i
                maxRight = i + p[i]

            if p[i] > maxLen:
                start = int((i - p[i] - 1) / 2)
                maxLen = p[i]

        return s[start:start+maxLen]