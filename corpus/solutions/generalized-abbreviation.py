class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        results = []

        def build(index, abbreviated, current):
            if index == len(word):
                if abbreviated:
                    current += str(abbreviated)
                results.append(current)
                return
            build(index + 1, abbreviated + 1, current)
            prefix = current + (str(abbreviated) if abbreviated else "")
            build(index + 1, 0, prefix + word[index])

        build(0, 0, "")
        return sorted(results)
