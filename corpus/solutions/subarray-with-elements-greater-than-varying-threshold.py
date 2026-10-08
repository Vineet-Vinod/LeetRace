from typing import List


class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        stack = []
        answer = len(nums) + 1
        for i, value in enumerate(nums + [0]):
            start = i
            while stack and stack[-1][1] >= value:
                left, minimum = stack.pop()
                start = left
                needed = threshold // minimum + 1
                if needed <= i - left:
                    answer = min(answer, needed)
            if value:
                stack.append((start, value))
        return answer if answer <= len(nums) else -1
