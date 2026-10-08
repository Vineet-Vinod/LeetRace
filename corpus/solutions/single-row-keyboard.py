class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        positions = {char: i for i, char in enumerate(keyboard)}
        current = total = 0
        for char in word:
            next_position = positions[char]
            total += abs(next_position - current)
            current = next_position
        return total
