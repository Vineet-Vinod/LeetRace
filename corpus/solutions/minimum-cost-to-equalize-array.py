from typing import List


class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        n, total, low, high = len(nums), sum(nums), min(nums), max(nums)
        if n <= 2 or cost2 >= 2 * cost1:
            return ((n * high - total) * cost1) % (10**9 + 7)
        threshold = max(high, (total - 2 * low + n - 3) // (n - 2))
        answer = 10**40
        for target in {high, threshold - 1, threshold, threshold + 1, threshold + 2}:
            if target < high:
                continue
            deficit = n * target - total
            largest = target - low
            pairs = min(deficit // 2, deficit - largest)
            answer = min(answer, pairs * cost2 + (deficit - 2 * pairs) * cost1)
        return answer % (10**9 + 7)
