class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()  # Sort the list first
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:  # Skip duplicates
                continue
            target = -num
            left, right = i + 1, len(nums) - 1  # Use two pointers
            while left < right:
                if nums[left] + nums[right] == target:
                    res.add(tuple(sorted([num, nums[left], nums[right]])))
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:  # Skip duplicates
                        left += 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return list(res)
