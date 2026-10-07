from typing import List
from math import comb


class Solution:
    def getProbability(self, balls: List[int]) -> float:
        half = sum(balls) // 2
        dp = {(0, 0): 1}
        for count in balls:
            nxt = {}
            for (used, diff), ways in dp.items():
                for first in range(count + 1):
                    if used + first > half:
                        continue
                    key = (used + first, diff + int(first > 0) - int(first < count))
                    nxt[key] = nxt.get(key, 0) + ways * comb(count, first)
            dp = nxt
        return dp.get((half, 0), 0) / comb(2 * half, half)
