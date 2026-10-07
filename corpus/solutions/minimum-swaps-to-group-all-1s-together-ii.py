class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = sum(nums)
        if ones <= 1:
            return 0
        doubled = nums + nums
        current_ones = sum(doubled[:ones])
        maximum = current_ones
        for end in range(ones, ones + len(nums) - 1):
            current_ones += doubled[end] - doubled[end - ones]
            maximum = max(maximum, current_ones)
        return ones - maximum
