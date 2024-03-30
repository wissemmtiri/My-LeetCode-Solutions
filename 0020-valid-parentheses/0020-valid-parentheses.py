class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapper = {"(": ")", "{": "}", "[": "]"}
        for char in s : 
            if char in mapper.keys() :
                stack.append(char)
            elif char in mapper.values() :
                if not stack or mapper[stack.pop()] != char :
                    return False
        return not stack