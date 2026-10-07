class Solution:
    def minTimeToType(self, word: str) -> int:
        total = 0
        position = 0
        for char in word:
            target = ord(char) - ord("a")
            distance = abs(target - position)
            total += min(distance, 26 - distance) + 1
            position = target
        return total
