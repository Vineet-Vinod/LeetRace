from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        from collections import deque

        queue: deque[tuple[int, int]] = deque()
        answer = nums[0]
        for i, value in enumerate(nums):
            while queue and queue[0][0] < i - k:
                queue.popleft()
            current = value + max(0, queue[0][1] if queue else 0)
            answer = max(answer, current)
            while queue and queue[-1][1] <= current:
                queue.pop()
            queue.append((i, current))
        return answer
