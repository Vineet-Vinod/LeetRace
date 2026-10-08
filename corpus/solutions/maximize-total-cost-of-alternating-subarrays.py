class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        negative_infinity = -(10**100)
        odd_length = negative_infinity
        even_length = 0
        for value in nums:
            next_odd = max(odd_length, even_length) + value
            next_even = odd_length - value
            odd_length, even_length = next_odd, next_even
        return max(odd_length, even_length)
