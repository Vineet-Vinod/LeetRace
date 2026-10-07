from __future__ import annotations
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for value in arr:
            if not stack or value >= stack[-1]:
                stack.append(value)
            else:
                maximum = stack.pop()
                while stack and stack[-1] > value:
                    stack.pop()
                stack.append(maximum)
        return len(stack)
