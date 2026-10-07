from __future__ import annotations
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        lm = rm = answer = 0
        while left <= right:
            if lm <= rm:
                lm = max(lm, height[left])
                answer += lm - height[left]
                left += 1
            else:
                rm = max(rm, height[right])
                answer += rm - height[right]
                right -= 1
        return answer
