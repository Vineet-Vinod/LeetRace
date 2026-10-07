class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        values = sorted(nums)
        left, right = 0, len(values) - 1
        best = -1
        while left < right:
            total = values[left] + values[right]
            if total < k:
                best = max(best, total)
                left += 1
            else:
                right -= 1
        return best
