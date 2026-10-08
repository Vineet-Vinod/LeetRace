class Solution:
    def wordSquares(self, words: list[str]) -> list[list[str]]:
        width = len(words[0])
        prefixes = {}
        for word in sorted(words):
            for i in range(width):
                prefixes.setdefault(word[:i], []).append(word)
        result = []

        def search(square):
            depth = len(square)
            if depth == width:
                result.append(square.copy())
                return
            prefix = "".join(row[depth] for row in square)
            for word in prefixes.get(prefix, []):
                square.append(word)
                search(square)
                square.pop()

        search([])
        return result
