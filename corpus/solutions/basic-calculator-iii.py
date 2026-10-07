class Solution:
    def calculate(self, s: str) -> int:
        values = []
        ops = []
        priority = {"+": 1, "-": 1, "*": 2, "/": 2, "u+": 3, "u-": 3}
        expecting_operand = True

        def apply():
            op = ops.pop()
            if op in ("u+", "u-"):
                values.append(values.pop() * (-1 if op == "u-" else 1))
                return
            b, a = values.pop(), values.pop()
            if op == "+":
                values.append(a + b)
            elif op == "-":
                values.append(a - b)
            elif op == "*":
                values.append(a * b)
            else:
                values.append((abs(a) // abs(b)) * (-1 if (a < 0) != (b < 0) else 1))

        i = 0
        while i < len(s):
            ch = s[i]
            if ch.isdigit():
                value = 0
                while i < len(s) and s[i].isdigit():
                    value = value * 10 + int(s[i])
                    i += 1
                values.append(value)
                expecting_operand = False
                continue
            if ch == "(":
                ops.append(ch)
                expecting_operand = True
            elif ch == ")":
                while ops[-1] != "(":
                    apply()
                ops.pop()
                expecting_operand = False
            elif ch in priority:
                if expecting_operand and ch in "+-":
                    ops.append("u" + ch)
                    i += 1
                    continue
                while ops and ops[-1] != "(" and priority[ops[-1]] >= priority[ch]:
                    apply()
                ops.append(ch)
                expecting_operand = True
            i += 1
        while ops:
            apply()
        return values[0]
