class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "" :
            return 0
        needleLength = len(needle) 
        for i in range(len(haystack) - needleLength + 1) :
            if haystack[i:i+needleLength] == needle : 
                return i
        return -1