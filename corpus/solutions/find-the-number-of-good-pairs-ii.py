from collections import Counter


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        frequencies = Counter(nums1)
        divisors = Counter(value * k for value in nums2 if value * k <= max(nums1))
        maximum = max(nums1)
        total = 0
        for divisor, multiplicity in divisors.items():
            multiples = sum(
                frequencies[multiple]
                for multiple in range(divisor, maximum + 1, divisor)
            )
            total += multiplicity * multiples
        return total
