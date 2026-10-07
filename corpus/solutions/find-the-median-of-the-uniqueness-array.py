from __future__ import annotations
from typing import List


class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        from collections import defaultdict

        n = len(nums)
        rank = (n * (n + 1) // 2 + 1) // 2

        def enough(k):
            counts = defaultdict(int)
            left = distinct = total = 0
            for right, value in enumerate(nums):
                distinct += counts[value] == 0
                counts[value] += 1
                while distinct > k:
                    v = nums[left]
                    counts[v] -= 1
                    distinct -= counts[v] == 0
                    left += 1
                total += right - left + 1
            return total >= rank

        low, high = 1, len(set(nums))
        while low < high:
            mid = (low + high) // 2
            if enough(mid):
                high = mid
            else:
                low = mid + 1
        return low
