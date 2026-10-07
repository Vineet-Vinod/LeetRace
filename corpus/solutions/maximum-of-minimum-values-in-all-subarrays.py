class Solution:
    def findMaximums(self, nums: List[int]) -> List[int]:
        size = len(nums)
        best = [0] * (size + 1)
        stack = []
        for index in range(size + 1):
            while stack and (index == size or nums[stack[-1]] > nums[index]):
                position = stack.pop()
                left = stack[-1] if stack else -1
                width = index - left - 1
                best[width] = max(best[width], nums[position])
            if index < size:
                stack.append(index)
        for width in range(size - 1, 0, -1):
            best[width] = max(best[width], best[width + 1])
        return [best[width] for width in range(1, size + 1)]
