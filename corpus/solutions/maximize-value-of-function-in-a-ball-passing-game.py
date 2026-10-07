from typing import List


class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        n = len(receiver)
        position = list(range(n))
        score = list(range(n))
        jump = receiver[:]
        gain = receiver[:]
        while k:
            if k & 1:
                for i in range(n):
                    score[i] += gain[position[i]]
                    position[i] = jump[position[i]]
            k >>= 1
            if k:
                gain = [gain[i] + gain[jump[i]] for i in range(n)]
                jump = [jump[jump[i]] for i in range(n)]
        return max(score)
