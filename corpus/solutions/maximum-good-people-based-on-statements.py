from typing import List


class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        needs_good = [
            sum(1 << j for j in range(n) if row[j] == 1) for row in statements
        ]
        needs_bad = [sum(1 << j for j in range(n) if row[j] == 0) for row in statements]
        best = 0
        for mask in range(1 << n):
            count = mask.bit_count()
            if count <= best:
                continue
            if all(
                not (mask >> i & 1)
                or (mask & needs_good[i] == needs_good[i] and not mask & needs_bad[i])
                for i in range(n)
            ):
                best = count
        return best
