class Solution:
    def reverseParentheses(self, s: str) -> str:
        pairs = {}
        stack = []
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                j = stack.pop()
                pairs[i] = j
                pairs[j] = i
        out = []
        i = 0
        step = 1
        while 0 <= i < len(s):
            if s[i] in "()":
                i = pairs[i]
                step = -step
            else:
                out.append(s[i])
            i += step
        return "".join(out)
