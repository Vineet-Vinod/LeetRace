class Solution:
    def maximumLengthOfRanges(self, nums: list[int]) -> list[int]:
        size = len(nums)
        left = [-1] * size
        right = [size] * size
        stack: list[int] = []
        for index, value in enumerate(nums):
            while stack and nums[stack[-1]] < value:
                right[stack.pop()] = index
            if stack:
                left[index] = stack[-1]
            stack.append(index)
        return [right[index] - left[index] - 1 for index in range(size)]
