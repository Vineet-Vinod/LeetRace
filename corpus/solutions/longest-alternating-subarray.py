class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        best = 0
        for start in range(len(nums) - 1):
            if nums[start + 1] - nums[start] != 1:
                continue
            length = 2
            while start + length < len(nums) and nums[start + length] - nums[
                start + length - 1
            ] == (-1 if length % 2 == 0 else 1):
                length += 1
            best = max(best, length)
        return best if best else -1
