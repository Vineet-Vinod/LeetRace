class Solution:
    def clumsy(self, n: int) -> int:
        values = list(range(n, 0, -1))
        stack = [values[0]]
        for i in range(1, n):
            op = (i - 1) % 4
            if op == 0:
                stack[-1] *= values[i]
            elif op == 1:
                stack[-1] = int(stack[-1] / values[i])
            elif op == 2:
                stack.append(values[i])
            else:
                stack.append(-values[i])
        return sum(stack)
