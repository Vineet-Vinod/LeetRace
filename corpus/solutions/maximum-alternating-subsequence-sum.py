class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        even = 0
        odd = 0
        for value in nums:
            even, odd = max(even, odd + value), max(odd, even - value)
        return even
