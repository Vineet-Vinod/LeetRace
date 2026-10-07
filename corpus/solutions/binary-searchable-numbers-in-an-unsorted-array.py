class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        suffix_min = [float("inf")] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            suffix_min[i] = min(nums[i + 1], suffix_min[i + 1])
        prefix_max = float("-inf")
        count = 0
        for i, value in enumerate(nums):
            if prefix_max < value and value < suffix_min[i]:
                count += 1
            prefix_max = max(prefix_max, value)
        return count
