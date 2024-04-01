class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = (digits[-1] + 1) // 10
        digits[-1] = (digits[-1] + 1) % 10
        counter = len(digits) - 2
        while carry and counter >= 0:
            res = digits[counter] + carry
            carry = res // 10
            digits[counter] = res % 10
            counter -= 1
        if carry:
            digits = [1] + digits
        return digits