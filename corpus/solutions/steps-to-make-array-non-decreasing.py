class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = []
        answer = 0
        for value in nums:
            steps = 0
            while stack and stack[-1][0] <= value:
                steps = max(steps, stack.pop()[1])
            if stack:
                steps += 1
            else:
                steps = 0
            answer = max(answer, steps)
            stack.append((value, steps))
        return answer
