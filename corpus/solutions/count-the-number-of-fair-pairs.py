class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        values = sorted(nums)

        def count_at_most(limit: int) -> int:
            left, right = 0, len(values) - 1
            total = 0
            while left < right:
                if values[left] + values[right] <= limit:
                    total += right - left
                    left += 1
                else:
                    right -= 1
            return total

        return count_at_most(upper) - count_at_most(lower - 1)
