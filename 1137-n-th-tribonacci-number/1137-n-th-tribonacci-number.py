class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        Tn, Tn1, Tn2 = 0, 1, 1
        for i in range(3, n + 1):
            c = Tn + Tn1 + Tn2
            Tn, Tn1, Tn2 = Tn1, Tn2, c
        return c