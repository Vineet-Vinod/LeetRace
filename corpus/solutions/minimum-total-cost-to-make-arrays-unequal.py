from typing import List
from collections import Counter


class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        counts = Counter()
        total = count = 0
        for i, (a, b) in enumerate(zip(nums1, nums2)):
            if a == b:
                counts[a] += 1
                count += 1
                total += i
        if not counts:
            return 0
        value, frequency = counts.most_common(1)[0]
        for i, (a, b) in enumerate(zip(nums1, nums2)):
            if count >= 2 * frequency:
                break
            if a != b and a != value and b != value:
                count += 1
                total += i
        return total if count >= 2 * frequency else -1
