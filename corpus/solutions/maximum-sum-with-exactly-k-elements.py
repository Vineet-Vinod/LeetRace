class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        largest = max(nums)
        return k * largest + k * (k - 1) // 2
