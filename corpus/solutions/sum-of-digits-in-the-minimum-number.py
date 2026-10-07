class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        digit_sum = sum(int(d) for d in str(min(nums)))
        return 0 if digit_sum % 2 else 1
