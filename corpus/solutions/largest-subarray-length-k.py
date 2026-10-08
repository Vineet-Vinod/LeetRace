class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        start = max(range(len(nums) - k + 1), key=lambda index: nums[index])
        return nums[start : start + k]
