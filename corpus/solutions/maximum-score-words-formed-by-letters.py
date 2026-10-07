from collections import Counter
from typing import List


class Solution:
    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        available = Counter(letters)
        needs = [Counter(word) for word in words]
        values = [
            sum(score[ord(c) - 97] * count for c, count in need.items())
            for need in needs
        ]

        def search(i):
            if i == len(words):
                return 0
            best = search(i + 1)
            need = needs[i]
            if all(available[c] >= count for c, count in need.items()):
                available.subtract(need)
                best = max(best, values[i] + search(i + 1))
                available.update(need)
            return best

        return search(0)
