class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = 0
        best_difference = float("inf")
        best_index = 0
        for index, value in enumerate(nums):
            prefix += value
            right_count = len(nums) - index - 1
            right_sum = total - prefix
            right_average = right_sum // right_count if right_count else 0
            difference = abs(prefix // (index + 1) - right_average)
            if difference < best_difference:
                best_difference = difference
                best_index = index
        return best_index
