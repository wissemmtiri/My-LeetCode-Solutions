class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        start = len(stones)
        for jewel in jewels:
            stones = stones.replace(jewel, '')
        return start - len(stones)