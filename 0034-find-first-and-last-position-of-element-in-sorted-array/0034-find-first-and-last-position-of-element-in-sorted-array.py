class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        indexes = [-1, -1]
        if not nums:
            return indexes
        index = 0
        while index < len(nums) and nums[index] != target:
            index += 1
        if index == len(nums):
            return indexes
        indexes[0] = index
        length = 0
        while index + length < len(nums) and nums[index + length] == target:
            length += 1
        return [indexes[0], indexes[0] + length - 1]