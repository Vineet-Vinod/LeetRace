from typing import List
from math import comb


class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        v, h = destination
        answer = []
        while h and v:
            count = comb(h + v - 1, v)
            if k <= count:
                answer.append("H")
                h -= 1
            else:
                answer.append("V")
                v -= 1
                k -= count
        return "".join(answer) + "H" * h + "V" * v
