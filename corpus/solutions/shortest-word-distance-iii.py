class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        best = len(wordsDict)
        last1 = last2 = -1
        if word1 == word2:
            for i, w in enumerate(wordsDict):
                if w == word1:
                    if last1 >= 0:
                        best = min(best, i - last1)
                    last1 = i
        else:
            for i, w in enumerate(wordsDict):
                if w == word1:
                    last1 = i
                elif w == word2:
                    last2 = i
                if last1 >= 0 and last2 >= 0:
                    best = min(best, abs(last1 - last2))
        return best
