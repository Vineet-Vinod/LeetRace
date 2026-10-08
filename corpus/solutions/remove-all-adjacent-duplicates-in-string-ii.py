class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack: List[Tuple[str, int]] = []
        for char in s:
            if stack and stack[-1][0] == char:
                count = stack[-1][1] + 1
                stack[-1] = (char, count)
                if count == k:
                    stack.pop()
            else:
                stack.append((char, 1))
        return "".join(char * count for char, count in stack)
