class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        answer = 0
        for i, h in enumerate(heights + [0]):
            start = i
            while stack and stack[-1][1] > h:
                start, value = stack.pop()
                answer = max(answer, value * (i - start))
            stack.append((start, h))
        return answer
