from collections import deque


class Solution:
    def maximumRobots(
        self, chargeTimes: List[int], runningCosts: List[int], budget: int
    ) -> int:
        queue = deque()
        left = total = answer = 0
        for right, charge in enumerate(chargeTimes):
            total += runningCosts[right]
            while queue and chargeTimes[queue[-1]] <= charge:
                queue.pop()
            queue.append(right)
            while (
                left <= right
                and chargeTimes[queue[0]] + (right - left + 1) * total > budget
            ):
                total -= runningCosts[left]
                if queue[0] == left:
                    queue.popleft()
                left += 1
            answer = max(answer, right - left + 1)
        return answer
