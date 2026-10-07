class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        operations = index = 0
        while index < len(word) - 1:
            if abs(ord(word[index]) - ord(word[index + 1])) <= 1:
                operations += 1
                index += 2
            else:
                index += 1
        return operations
