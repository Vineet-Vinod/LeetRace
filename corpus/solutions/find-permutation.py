class Solution:
    def findPermutation(self, s: str) -> List[int]:
        stack = []
        result = []
        for i in range(len(s) + 1):
            stack.append(i + 1)
            if i == len(s) or s[i] == "I":
                result.extend(reversed(stack))
                stack.clear()
        return result
