from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        queue = deque()
        answer = []
        for i, value in enumerate(nums):
            while queue and queue[0] <= i - k:
                queue.popleft()
            while queue and nums[queue[-1]] <= value:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                answer.append(nums[queue[0]])
        return answer
