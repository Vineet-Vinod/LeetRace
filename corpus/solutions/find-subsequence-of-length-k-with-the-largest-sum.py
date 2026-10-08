class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        chosen = set(sorted(range(len(nums)), key=lambda i: (-nums[i], i))[:k])
        return [value for i, value in enumerate(nums) if i in chosen]
