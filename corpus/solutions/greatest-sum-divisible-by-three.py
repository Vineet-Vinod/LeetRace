class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        best = [0, -(10**18), -(10**18)]
        for value in nums:
            previous = best[:]
            for remainder in range(3):
                total = previous[remainder] + value
                new_remainder = total % 3
                best[new_remainder] = max(best[new_remainder], total)
        return best[0]
