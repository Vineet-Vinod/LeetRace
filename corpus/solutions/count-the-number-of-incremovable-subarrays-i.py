class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for left in range(n):
            for right in range(left, n):
                remaining = nums[:left] + nums[right + 1 :]
                if all(
                    remaining[i - 1] < remaining[i] for i in range(1, len(remaining))
                ):
                    count += 1
        return count
