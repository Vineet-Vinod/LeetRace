from typing import List


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        mod = 10**9 + 7
        total = [1] + [0] * n
        endings = [[0] * 6 for _ in range(n + 1)]
        for length in range(1, n + 1):
            for face, limit in enumerate(rollMax):
                value = total[length - 1]
                if length == limit + 1:
                    value -= 1
                elif length > limit + 1:
                    previous = length - limit - 1
                    value -= total[previous] - endings[previous][face]
                endings[length][face] = value % mod
            total[length] = sum(endings[length]) % mod
        return total[n]
