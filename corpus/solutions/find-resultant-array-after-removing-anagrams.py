class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result: list[str] = []
        previous: tuple[str, ...] | None = None
        for word in words:
            signature = tuple(sorted(word))
            if signature != previous:
                result.append(word)
                previous = signature
        return result
