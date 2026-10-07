class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        best = 0
        largest_left = nums[0]
        best_difference = 0
        for value in nums[1:]:
            best = max(best, best_difference * value)
            best_difference = max(best_difference, largest_left - value)
            largest_left = max(largest_left, value)
        return best
