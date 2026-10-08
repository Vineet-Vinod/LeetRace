class Solution:
    def minimumTime(self, s: str) -> int:
        answer = len(s)
        left = 0
        for i, char in enumerate(s):
            if char == "1":
                left = min(left + 2, i + 1)
            answer = min(answer, left + len(s) - i - 1)
        return answer
