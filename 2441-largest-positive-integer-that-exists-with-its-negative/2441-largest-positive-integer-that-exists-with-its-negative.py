class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        index = len(nums) - 1
        while nums[index] > 0 and index > 0:
            if -nums[index] in nums:
                return nums[index]
            index -= 1
        return -1