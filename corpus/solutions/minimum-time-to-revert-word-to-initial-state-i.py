class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        length = len(word)
        turns = 1
        while turns * k < length:
            suffix_start = turns * k
            if word[suffix_start:] == word[: length - suffix_start]:
                return turns
            turns += 1
        return turns
