class Solution:
    def smallestSubsequence(self, s: str) -> str:
        remaining = Counter(s)
        stack = []
        present = set()
        for char in s:
            remaining[char] -= 1
            if char in present:
                continue
            while stack and stack[-1] > char and remaining[stack[-1]] > 0:
                present.remove(stack.pop())
            stack.append(char)
            present.add(char)
        return "".join(stack)
