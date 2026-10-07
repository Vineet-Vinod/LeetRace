class Solution:
    def countSpecialSubsequences(self, nums: list[int]) -> int:
        counts = [0, 0, 0]
        for x in nums:
            counts[x] = (2 * counts[x] + (counts[x - 1] if x else 1)) % 1000000007
        return counts[2]
