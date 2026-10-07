class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        place = 1
        while place <= max(nums):
            counts = [0] * 10
            for x in nums:
                counts[x // place % 10] += 1
            total += sum(c * (n - c) for c in counts) // 2
            place *= 10
        return total
