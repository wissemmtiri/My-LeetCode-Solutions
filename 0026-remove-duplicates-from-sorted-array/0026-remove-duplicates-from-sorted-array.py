class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 1
        index = 0
        reference = nums[0]
        for num in nums[1:]:
            if num != reference:
                reference = num
                counter += 1
                index += 1
                nums[index] = num
        return counter