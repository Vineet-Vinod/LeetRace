class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @cache
        def compute(start: int, end: int) -> List[int]:
            results: List[int] = []
            for index in range(start, end):
                if expression[index] in "+-*":
                    left_values = compute(start, index)
                    right_values = compute(index + 1, end)
                    for left in left_values:
                        for right in right_values:
                            if expression[index] == "+":
                                results.append(left + right)
                            elif expression[index] == "-":
                                results.append(left - right)
                            else:
                                results.append(left * right)
            if not results:
                return [int(expression[start:end])]
            return results

        return sorted(compute(0, len(expression)))
