class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        best = 0
        start = 0
        while start < len(nums):
            if nums[start] % 2 or nums[start] > threshold:
                start += 1
                continue
            end = start + 1
            while (
                end < len(nums)
                and nums[end] <= threshold
                and nums[end] % 2 != nums[end - 1] % 2
            ):
                end += 1
            best = max(best, end - start)
            start = end
        return best
