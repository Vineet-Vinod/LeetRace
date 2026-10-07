from typing import List


class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack: list[int] = []
        answer = 0
        for value in nums:
            while stack and stack[-1] > value:
                stack.pop()
            stack.append(value)
            answer += len(stack)
        return answer
