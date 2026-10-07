class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        values = []
        operators = []

        def combine():
            b, a = values.pop(), values.pop()
            operator = operators.pop()
            costs = [10**9, 10**9]
            for x in range(2):
                for y in range(2):
                    for op in "&|":
                        result = x & y if op == "&" else x | y
                        costs[result] = min(
                            costs[result], a[x] + b[y] + (operator != op)
                        )
            values.append(costs)

        for c in expression:
            if c in "01":
                values.append([int(c != "0"), int(c != "1")])
                if operators and operators[-1] != "(":
                    combine()
            elif c == "(":
                operators.append(c)
            elif c == ")":
                operators.pop()
                if operators and operators[-1] != "(":
                    combine()
            else:
                operators.append(c)
        return max(values[0])
