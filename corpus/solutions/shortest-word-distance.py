class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        last_first = last_second = None
        best = len(wordsDict)
        for index, word in enumerate(wordsDict):
            if word == word1:
                last_first = index
            elif word == word2:
                last_second = index
            if last_first is not None and last_second is not None:
                best = min(best, abs(last_first - last_second))
        return best
