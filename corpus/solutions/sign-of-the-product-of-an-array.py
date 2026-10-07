class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        return -1 if sum(value < 0 for value in nums) % 2 else 1
