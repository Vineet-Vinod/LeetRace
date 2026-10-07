class Solution:
    def robotWithString(self, s: str) -> str:
        remaining = [0] * 26
        for char in s:
            remaining[ord(char) - ord("a")] += 1
        stack = []
        output = []
        for char in s:
            stack.append(char)
            remaining[ord(char) - ord("a")] -= 1
            smallest = next((i for i, count in enumerate(remaining) if count), 26)
            while stack and ord(stack[-1]) - ord("a") <= smallest:
                output.append(stack.pop())
        return "".join(output)
