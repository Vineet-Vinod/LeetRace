from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        values = sorted(set(nums))
        bit = [0] * (len(values) + 1)
        answer = 0
        for count, value in enumerate(nums):
            i = bisect_right(values, 2 * value)
            prefix = 0
            while i:
                prefix += bit[i]
                i -= i & -i
            answer += count - prefix
            i = bisect_left(values, value) + 1
            while i < len(bit):
                bit[i] += 1
                i += i & -i
        return answer
