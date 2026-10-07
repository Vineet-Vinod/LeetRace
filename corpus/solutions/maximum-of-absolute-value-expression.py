class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        expressions = [[], [], [], []]
        for index, (first, second) in enumerate(zip(arr1, arr2)):
            values = (
                first + second + index,
                first + second - index,
                first - second + index,
                first - second - index,
            )
            for expression, value in zip(expressions, values):
                expression.append(value)
        return max(max(values) - min(values) for values in expressions)
