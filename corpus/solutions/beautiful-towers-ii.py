class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        size = len(maxHeights)
        left_sums = [0] * size
        stack = []
        for index, height in enumerate(maxHeights):
            while stack and maxHeights[stack[-1]] > height:
                stack.pop()
            previous = stack[-1] if stack else -1
            left_sums[index] = height * (index - previous) + (
                left_sums[previous] if previous >= 0 else 0
            )
            stack.append(index)
        right_sums = [0] * size
        stack.clear()
        for index in range(size - 1, -1, -1):
            height = maxHeights[index]
            while stack and maxHeights[stack[-1]] > height:
                stack.pop()
            following = stack[-1] if stack else size
            right_sums[index] = height * (following - index) + (
                right_sums[following] if following < size else 0
            )
            stack.append(index)
        return max(left_sums[i] + right_sums[i] - maxHeights[i] for i in range(size))
