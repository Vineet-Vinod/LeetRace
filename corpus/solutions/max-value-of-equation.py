from collections import deque


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        queue = deque()
        answer = -(10**30)
        for x, y in points:
            while queue and x - queue[0][0] > k:
                queue.popleft()
            if queue:
                answer = max(answer, x + y + queue[0][1])
            while queue and queue[-1][1] <= y - x:
                queue.pop()
            queue.append((x, y - x))
        return answer
