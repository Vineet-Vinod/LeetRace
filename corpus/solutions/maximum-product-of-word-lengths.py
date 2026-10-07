class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks = []
        for word in words:
            mask = 0
            for char in set(word):
                mask |= 1 << (ord(char) - ord("a"))
            masks.append(mask)
        best = 0
        for first in range(len(words)):
            for second in range(first + 1, len(words)):
                if masks[first] & masks[second] == 0:
                    best = max(best, len(words[first]) * len(words[second]))
        return best
