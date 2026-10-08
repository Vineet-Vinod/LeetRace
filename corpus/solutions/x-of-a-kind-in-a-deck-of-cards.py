class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from collections import Counter
        from math import gcd

        divisor = 0
        for count in Counter(deck).values():
            divisor = gcd(divisor, count)
        return divisor >= 2
