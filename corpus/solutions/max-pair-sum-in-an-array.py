class Solution:
    def maxSum(self, nums: List[int]) -> int:
        largest_by_digit: dict[int, int] = {}
        best = -1
        for value in nums:
            largest_digit = max(int(char) for char in str(value))
            if largest_digit in largest_by_digit:
                best = max(best, value + largest_by_digit[largest_digit])
            largest_by_digit[largest_digit] = max(
                largest_by_digit.get(largest_digit, 0), value
            )
        return best
