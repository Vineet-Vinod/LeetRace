class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        repeat = 0
        while word * (repeat + 1) in sequence:
            repeat += 1
        return repeat
