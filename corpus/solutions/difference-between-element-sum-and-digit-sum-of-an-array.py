class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digit_sum = sum(int(digit) for value in nums for digit in str(value))
        return abs(sum(nums) - digit_sum)
