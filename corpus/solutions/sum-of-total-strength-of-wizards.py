from __future__ import annotations
from typing import List


class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        mod = 10**9 + 7
        n = len(strength)
        left, right = [-1] * n, [n] * n
        stack = []
        for i, value in enumerate(strength):
            while stack and strength[stack[-1]] >= value:
                right[stack.pop()] = i
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        prefix = [0]
        for value in strength:
            prefix.append((prefix[-1] + value) % mod)
        pp = [0]
        for value in prefix:
            pp.append((pp[-1] + value) % mod)
        answer = 0
        for i, value in enumerate(strength):
            left_boundary, r = left[i], right[i]
            total = (i - left_boundary) * (pp[r + 1] - pp[i + 1]) - (r - i) * (
                pp[i + 1] - pp[left_boundary + 1]
            )
            answer = (answer + value * total) % mod
        return answer
