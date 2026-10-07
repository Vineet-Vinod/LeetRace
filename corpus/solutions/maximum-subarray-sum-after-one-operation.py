class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        without_square = nums[0]
        with_square = nums[0] * nums[0]
        best = with_square
        for value in nums[1:]:
            with_square = max(
                value * value, with_square + value, without_square + value * value
            )
            without_square = max(value, without_square + value)
            best = max(best, with_square)
        return best
