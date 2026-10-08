from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(heights)
        for i in range(len(heights) - 1, -1, -1):
            while stack and stack[-1] < heights[i]:
                stack.pop()
                ans[i] += 1
            if stack:
                ans[i] += 1
            stack.append(heights[i])
        return ans
