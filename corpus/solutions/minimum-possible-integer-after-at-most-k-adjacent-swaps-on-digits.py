from collections import deque


class Solution:
    def minInteger(self, num: str, k: int) -> str:
        n = len(num)
        positions = [deque() for _ in range(10)]
        for i, c in enumerate(num):
            positions[int(c)].append(i)
        bit = [0] * (n + 1)
        out = []
        for _ in range(n):
            for digit in range(10):
                if not positions[digit]:
                    continue
                pos = positions[digit][0]
                removed = 0
                i = pos + 1
                while i:
                    removed += bit[i]
                    i -= i & -i
                cost = pos - removed
                if cost <= k:
                    k -= cost
                    positions[digit].popleft()
                    out.append(str(digit))
                    i = pos + 1
                    while i <= n:
                        bit[i] += 1
                        i += i & -i
                    break
        return "".join(out)
