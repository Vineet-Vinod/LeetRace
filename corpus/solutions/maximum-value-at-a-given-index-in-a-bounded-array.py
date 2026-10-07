class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def side_sum(length: int, peak: int) -> int:
            descending = min(length, peak - 1)
            return descending * (2 * peak - descending - 1) // 2 + (length - descending)

        low, high = 1, maxSum
        while low < high:
            peak = (low + high + 1) // 2
            needed = peak + side_sum(index, peak) + side_sum(n - index - 1, peak)
            if needed <= maxSum:
                low = peak
            else:
                high = peak - 1
        return low
