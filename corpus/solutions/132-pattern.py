class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        middle = float("-inf")
        stack: list[int] = []
        for value in reversed(nums):
            if value < middle:
                return True
            while stack and stack[-1] < value:
                middle = max(middle, stack.pop())
            stack.append(value)
        return False
