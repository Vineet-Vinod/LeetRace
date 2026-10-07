from __future__ import annotations
from typing import List


class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        from itertools import combinations
        from collections import deque

        pre = [0] * n
        for a, b in relations:
            pre[b - 1] |= 1 << (a - 1)
        full = (1 << n) - 1
        queue = deque([(0, 0)])
        seen = {0}
        while queue:
            mask, semesters = queue.popleft()
            if mask == full:
                return semesters
            available = [
                i for i in range(n) if not mask >> i & 1 and pre[i] & mask == pre[i]
            ]
            choices = [available] if len(available) <= k else combinations(available, k)
            for choice in choices:
                nxt = mask
                for i in choice:
                    nxt |= 1 << i
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append((nxt, semesters + 1))
        return -1
