class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        best = [[0] * (n + 1) for _ in range(m + 1)]
        for value in strs:
            zeroes = value.count("0")
            ones = len(value) - zeroes
            for zero_limit in range(m, zeroes - 1, -1):
                for one_limit in range(n, ones - 1, -1):
                    best[zero_limit][one_limit] = max(
                        best[zero_limit][one_limit],
                        best[zero_limit - zeroes][one_limit - ones] + 1,
                    )
        return best[m][n]
