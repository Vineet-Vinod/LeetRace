class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack: list[int] = []
        for i, value in enumerate(nums):
            while stack and stack[-1] > value and len(stack) - 1 + len(nums) - i >= k:
                stack.pop()
            if len(stack) < k:
                stack.append(value)
        return stack
