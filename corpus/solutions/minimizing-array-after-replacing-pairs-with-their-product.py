class Solution:
    def minArrayLength(self, nums: List[int], k: int) -> int:
        if 0 in nums:
            return 1
        stack: list[int] = []
        for value in nums:
            if stack and stack[-1] * value <= k:
                stack[-1] *= value
            else:
                stack.append(value)
        return len(stack)
