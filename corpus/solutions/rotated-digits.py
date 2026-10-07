class Solution:
    def rotatedDigits(self, n: int) -> int:
        invalid = set("347")
        changed = set("2569")
        answer = 0
        for value in range(1, n + 1):
            digits = str(value)
            if any(char in invalid for char in digits):
                continue
            answer += any(char in changed for char in digits)
        return answer
