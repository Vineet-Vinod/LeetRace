from typing import List


class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        prefix = [1] * len(words)

        def abbreviate(word: str, length: int) -> str:
            if length >= len(word) - 2:
                return word
            return word[:length] + str(len(word) - length - 1) + word[-1]

        while True:
            groups: dict[str, list[int]] = {}
            for i, word in enumerate(words):
                key = abbreviate(word, prefix[i])
                groups.setdefault(key, []).append(i)
            conflicts = [indices for indices in groups.values() if len(indices) > 1]
            if not conflicts:
                return [abbreviate(word, prefix[i]) for i, word in enumerate(words)]
            for group in conflicts:
                for i in group:
                    prefix[i] += 1
