class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse(expression: str) -> tuple[int, int]:
            coefficient = 0
            constant = 0
            sign = 1
            index = 0
            while index < len(expression):
                if expression[index] in "+-":
                    sign = 1 if expression[index] == "+" else -1
                    index += 1
                end = index
                while end < len(expression) and expression[end].isdigit():
                    end += 1
                number = int(expression[index:end]) if end > index else 1
                if end < len(expression) and expression[end] == "x":
                    coefficient += sign * number
                    end += 1
                else:
                    constant += sign * number
                index = end
            return coefficient, constant

        left, right = equation.split("=")
        left_x, left_const = parse(left)
        right_x, right_const = parse(right)
        coefficient = left_x - right_x
        constant = right_const - left_const
        if coefficient == 0:
            return "Infinite solutions" if constant == 0 else "No solution"
        return f"x={constant // coefficient}"
