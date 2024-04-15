class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recursive(nums: list[int]):
            if len(nums) == 1:
                return [nums]
            result = []
            for i in range(len(nums)):
                for p in recursive(nums[:i] + nums[i + 1:]):
                    result.append([nums[i]] + p)
            return result

        return recursive(nums)