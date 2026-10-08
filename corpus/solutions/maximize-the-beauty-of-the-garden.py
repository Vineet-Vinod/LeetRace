from typing import List


class Solution:
    def maximumBeauty(self, flowers: List[int]) -> int:
        first: dict[int, int] = {}
        prefix = 0
        answer = -(10**30)
        for value in flowers:
            if value in first:
                answer = max(answer, prefix + value + first[value])
            first.setdefault(value, value - prefix - max(value, 0))
            prefix += max(value, 0)
        return answer
