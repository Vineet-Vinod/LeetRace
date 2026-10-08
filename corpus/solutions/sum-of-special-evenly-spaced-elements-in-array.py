from math import isqrt
from collections import Counter


class Solution:
    def solve(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        mod = 10**9 + 7
        frequency = Counter(step for _, step in queries)
        cached = {}
        for step, count in frequency.items():
            if step <= isqrt(n) and count > step:
                row = [0] * (n + step)
                for i in range(n - 1, -1, -1):
                    row[i] = (nums[i] + row[i + step]) % mod
                cached[step] = row
        return [
            cached[y][x] if y in cached else sum(nums[x::y]) % mod for x, y in queries
        ]
