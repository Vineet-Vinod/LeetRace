class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        remaining = s.count(letter)
        needed = repetition
        stack = []
        for i, char in enumerate(s):
            while stack and stack[-1] > char and len(stack) - 1 + len(s) - i >= k:
                if stack[-1] == letter and remaining <= needed:
                    break
                if stack.pop() == letter:
                    needed += 1
            if len(stack) < k:
                if char == letter:
                    stack.append(char)
                    needed -= 1
                elif k - len(stack) > needed:
                    stack.append(char)
            if char == letter:
                remaining -= 1
        return "".join(stack)
