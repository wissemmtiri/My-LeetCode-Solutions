class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        n = len(nums)
  
        for num, count in counts.items():
            if count > n // 2:
                return num