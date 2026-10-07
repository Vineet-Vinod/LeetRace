from __future__ import annotations
from typing import List


class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        ordered = sorted(items, reverse=True)
        seen = set()
        duplicates = []
        total = 0
        for profit, category in ordered[:k]:
            total += profit
            if category in seen:
                duplicates.append(profit)
            seen.add(category)
        answer = total + len(seen) ** 2
        for profit, category in ordered[k:]:
            if category not in seen and duplicates:
                total += profit - duplicates.pop()
                seen.add(category)
                answer = max(answer, total + len(seen) ** 2)
        return answer
