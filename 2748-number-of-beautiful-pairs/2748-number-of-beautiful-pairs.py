class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        count = 0
        def gcd(a, b): return a if b == 0 else gcd(b, a % b)

        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if gcd(int(str(nums[i])[0]), nums[j] % 10) == 1:
                    count += 1

        return count 