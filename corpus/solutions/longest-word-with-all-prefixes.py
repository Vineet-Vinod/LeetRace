class Solution:
    def longestWord(self, words: List[str]) -> str:
        available = set(words)
        valid = {""}
        best = ""
        for word in sorted(available, key=lambda value: (len(value), value)):
            if word[:-1] in valid:
                valid.add(word)
                if len(word) > len(best) or (len(word) == len(best) and word < best):
                    best = word
        return best
