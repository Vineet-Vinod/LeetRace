class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        minimum_index = nums.index(min(nums))
        maximum_index = n - 1 - nums[::-1].index(max(nums))
        return minimum_index + n - 1 - maximum_index - (minimum_index > maximum_index)
