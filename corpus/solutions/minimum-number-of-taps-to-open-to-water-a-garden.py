from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        farthest = [0] * (n + 1)
        for i, radius in enumerate(ranges):
            start = max(0, i - radius)
            farthest[start] = max(farthest[start], min(n, i + radius))
        end = reach = count = 0
        for i in range(n):
            reach = max(reach, farthest[i])
            if i == end:
                if reach <= i:
                    return -1
                count += 1
                end = reach
        return count
