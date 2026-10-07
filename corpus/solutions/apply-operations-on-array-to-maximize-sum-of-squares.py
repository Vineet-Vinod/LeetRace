from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        counts = [0] * 30
        for value in nums:
            while value:
                bit = (value & -value).bit_length() - 1
                counts[bit] += 1
                value &= value - 1
        answer = 0
        for rank in range(k):
            value = sum(1 << bit for bit, count in enumerate(counts) if count > rank)
            answer = (answer + value * value) % 1_000_000_007
        return answer
