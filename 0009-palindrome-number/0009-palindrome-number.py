class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        length = len(x)
        for i in range(length//2) :
            if x[i] != x[ length - 1 - i ] :
                return False
        return True
        