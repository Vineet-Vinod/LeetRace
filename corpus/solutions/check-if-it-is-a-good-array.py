from math import gcd


class Solution:
    def isGoodArray(self, nums: list[int]) -> bool:
        g = 0
        for x in nums:
            g = gcd(g, x)
        return g == 1
