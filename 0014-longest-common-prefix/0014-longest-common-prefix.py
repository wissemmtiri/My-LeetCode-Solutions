class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for index in range(min(len(x) for x in strs)) : 
            char = strs[0][index]
            if all(x[index] == char for x in strs) :
                  prefix += char 
            else :
                break
        return prefix
            