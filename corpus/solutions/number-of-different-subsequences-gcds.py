from typing import List


class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        from math import gcd

        present = set(nums)
        maximum = max(present)
        answer = 0
        for divisor in range(1, maximum + 1):
            current = 0
            for multiple in range(divisor, maximum + 1, divisor):
                if multiple in present:
                    current = gcd(current, multiple)
                    if current == divisor:
                        answer += 1
                        break
        return answer
