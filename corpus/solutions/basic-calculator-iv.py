from collections import Counter
import re


class Solution:
    def basicCalculatorIV(
        self, expression: str, evalvars: list[str], evalints: list[int]
    ) -> list[str]:
        values = dict(zip(evalvars, evalints))
        tokens = re.findall(r"[a-z]+|[0-9]+|[()+*-]", expression)
        pos = 0

        def add(a, b, sign=1):
            out = a.copy()
            for term, coefficient in b.items():
                out[term] += sign * coefficient
            return out

        def multiply(a, b):
            out = Counter()
            for x, u in a.items():
                for y, v in b.items():
                    out[tuple(sorted(x + y))] += u * v
            return out

        def atom():
            nonlocal pos
            token = tokens[pos]
            pos += 1
            if token == "(":
                result = expression_sum()
                pos += 1
                return result
            if token.isdigit():
                return Counter({(): int(token)})
            if token in values:
                return Counter({(): values[token]})
            return Counter({(token,): 1})

        def product():
            nonlocal pos
            result = atom()
            while pos < len(tokens) and tokens[pos] == "*":
                pos += 1
                result = multiply(result, atom())
            return result

        def expression_sum():
            nonlocal pos
            result = product()
            while pos < len(tokens) and tokens[pos] in ["+", "-"]:
                sign = 1 if tokens[pos] == "+" else -1
                pos += 1
                result = add(result, product(), sign)
            return result

        result = expression_sum()
        return [
            "*".join([str(result[t]), *t])
            for t in sorted(result, key=lambda t: (-len(t), t))
            if result[t]
        ]
