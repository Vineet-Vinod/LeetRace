from __future__ import annotations
from typing import List


class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        from math import gcd

        common = 0
        for value in numsDivide:
            common = gcd(common, value)
        for i, value in enumerate(sorted(nums)):
            if common % value == 0:
                return i
        return -1
