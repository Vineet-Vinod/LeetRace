class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        best_difference = nums[0] - nums[1]
        best = 0
        maximum_before = nums[0]
        for middle in range(1, len(nums) - 1):
            best_difference = max(best_difference, maximum_before - nums[middle])
            best = max(best, best_difference * nums[middle + 1])
            maximum_before = max(maximum_before, nums[middle])
        return best
