from typing import List
from collections import Counter


class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        if len(nums) <= 200:
            return sum(a // b for a in nums for b in nums) % 1000000007
        counts = Counter(nums)
        maximum = max(nums)
        prefix = [0] * (maximum + 1)
        for i in range(1, maximum + 1):
            prefix[i] = prefix[i - 1] + counts.get(i, 0)
        answer = 0
        for denominator, count in counts.items():
            for start in range(denominator, maximum + 1, denominator):
                end = min(start + denominator - 1, maximum)
                answer += (
                    count * (start // denominator) * (prefix[end] - prefix[start - 1])
                )
        return answer % 1000000007
