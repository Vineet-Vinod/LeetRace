class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(" ")
        height = max(map(len, words))
        result = []
        for column in range(height):
            line = "".join(
                word[column] if column < len(word) else " " for word in words
            )
            result.append(line.rstrip())
        return result
