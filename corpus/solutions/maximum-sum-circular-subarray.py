class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        max_ending = min_ending = 0
        max_sum = float("-inf")
        min_sum = float("inf")
        for value in nums:
            max_ending = max(value, max_ending + value)
            max_sum = max(max_sum, max_ending)
            min_ending = min(value, min_ending + value)
            min_sum = min(min_sum, min_ending)
        if max_sum < 0:
            return int(max_sum)
        return int(max(max_sum, total - min_sum))
