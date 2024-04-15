class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        for i in range(len(nums) - 2):
            if nums[i] + diff in nums[i + 1:]:
                j = nums.index(nums[i] + diff, i + 1)
                for k in range(j + 1, len(nums)):
                    if nums[k] == nums[j] + diff:
                        count += 1
                        break
        return count