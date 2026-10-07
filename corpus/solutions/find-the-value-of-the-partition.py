class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        ordered = sorted(nums)
        return min(
            ordered[index] - ordered[index - 1] for index in range(1, len(ordered))
        )
