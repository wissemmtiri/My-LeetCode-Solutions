class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        start = 0
        used = {}
        
        for i, char in enumerate(s) :
            if char in used and used[char] >= start :
                start = used[char] + 1
            else : 
                max_length = max(max_length, i - start + 1)
            used[char] = i
        
        return max_length