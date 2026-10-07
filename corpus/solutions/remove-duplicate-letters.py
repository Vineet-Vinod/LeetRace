class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        remaining = {c: s.count(c) for c in set(s)}
        stack = []
        present = set()
        for c in s:
            remaining[c] -= 1
            if c in present:
                continue
            while stack and stack[-1] > c and remaining[stack[-1]]:
                present.remove(stack.pop())
            stack.append(c)
            present.add(c)
        return "".join(stack)
