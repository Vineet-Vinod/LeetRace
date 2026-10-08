from typing import List
from math import gcd


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for value in nums:
            while stack:
                common = gcd(stack[-1], value)
                if common == 1:
                    break
                value = value // common * stack.pop()
            stack.append(value)
        return stack
