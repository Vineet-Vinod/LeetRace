class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        best = 0
        start = 0
        groups = 0
        for index, char in enumerate(word):
            if index and char < word[index - 1]:
                start = index
                groups = 1
            elif index == 0 or char != word[index - 1]:
                groups += 1
            if groups == 5:
                best = max(best, index - start + 1)
        return best
