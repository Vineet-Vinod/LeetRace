class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for row, word in enumerate(words):
            for column, char in enumerate(word):
                if (
                    column >= len(words)
                    or row >= len(words[column])
                    or words[column][row] != char
                ):
                    return False
        return True
