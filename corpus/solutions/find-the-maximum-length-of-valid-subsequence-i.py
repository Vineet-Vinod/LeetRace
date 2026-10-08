class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        parity_counts = [0, 0]
        alternating = [0, 0]
        for value in nums:
            parity = value % 2
            parity_counts[parity] += 1
            alternating[parity] = alternating[1 - parity] + 1
        return max(*parity_counts, *alternating)
