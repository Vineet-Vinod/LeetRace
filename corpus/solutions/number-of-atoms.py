from collections import Counter


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack: list[Counter[str]] = [Counter()]
        i = 0

        def count(start: int) -> tuple[int, int]:
            end = start
            while end < len(formula) and formula[end].isdigit():
                end += 1
            return (int(formula[start:end]) if end > start else 1), end

        while i < len(formula):
            ch = formula[i]
            if ch == "(":
                stack.append(Counter())
                i += 1
            elif ch == ")":
                multiplier, i = count(i + 1)
                group = stack.pop()
                for name, amount in group.items():
                    stack[-1][name] += amount * multiplier
            else:
                j = i + 1
                while j < len(formula) and formula[j].islower():
                    j += 1
                name = formula[i:j]
                amount, i = count(j)
                stack[-1][name] += amount
        return "".join(
            name + (str(amount) if amount > 1 else "")
            for name, amount in sorted(stack[0].items())
        )
