class Solution:
    def fixedRatio(self, s: str, num1: int, num2: int) -> int:
        counts = {0: 1}
        difference = answer = 0
        for char in s:
            difference += num2 if char == "0" else -num1
            answer += counts.get(difference, 0)
            counts[difference] = counts.get(difference, 0) + 1
        return answer
