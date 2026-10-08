from math import comb


class Solution:
    def waysToReachStair(self, k: int) -> int:
        answer = 0
        for jumps in range(31):
            down = (1 << jumps) - k
            if 0 <= down <= jumps + 1:
                answer += comb(jumps + 1, down)
        return answer
