from typing import List


class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        stack = []
        dp = [0] * len(books)
        for i, value in enumerate(books):
            while stack and books[stack[-1]] - stack[-1] >= value - i:
                stack.pop()
            previous = stack[-1] if stack else -1
            length = min(value, i - previous)
            dp[i] = length * (2 * value - length + 1) // 2
            if previous >= 0:
                dp[i] += dp[previous]
            stack.append(i)
        return max(dp)
