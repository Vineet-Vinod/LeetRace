class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = [float("inf")]
        answer = 0
        for value in arr:
            while stack[-1] <= value:
                middle = stack.pop()
                answer += middle * min(stack[-1], value)
            stack.append(value)
        while len(stack) > 2:
            answer += stack.pop() * stack[-1]
        return answer
