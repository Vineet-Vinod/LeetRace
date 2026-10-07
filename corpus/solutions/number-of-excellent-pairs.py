from collections import Counter


class Solution:
    def countExcellentPairs(self, nums: list[int], k: int) -> int:
        counts = Counter(x.bit_count() for x in set(nums))
        return sum(
            c * d for a, c in counts.items() for b, d in counts.items() if a + b >= k
        )
