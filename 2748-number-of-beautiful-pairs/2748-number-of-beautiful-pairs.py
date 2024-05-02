class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        count = 0

        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if math.gcd(int(str(nums[i])[0]), nums[j] % 10) == 1:
                    count += 1

        return count 