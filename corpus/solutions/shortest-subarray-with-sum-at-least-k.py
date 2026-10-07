from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        from collections import deque

        queue = deque([(0, 0)])
        total = 0
        best = len(nums) + 1
        for i, value in enumerate(nums, 1):
            total += value
            while queue and total - queue[0][1] >= k:
                previous, _ = queue.popleft()
                best = min(best, i - previous)
            while queue and total <= queue[-1][1]:
                queue.pop()
            queue.append((i, total))
        return best if best <= len(nums) else -1
