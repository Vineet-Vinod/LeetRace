from math import gcd
from collections import Counter


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        counts = Counter(gcd(x, k) for x in nums)
        answer = 0
        keys = sorted(counts)
        for i, a in enumerate(keys):
            for b in keys[i:]:
                if a * b % k == 0:
                    answer += (
                        counts[a] * (counts[a] - 1) // 2
                        if a == b
                        else counts[a] * counts[b]
                    )
        return answer
