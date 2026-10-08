class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        distinct = set(words)
        endings = {word[i:] for word in distinct for i in range(1, len(word))}
        return sum(len(word) + 1 for word in distinct if word not in endings)
