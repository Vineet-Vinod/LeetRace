class Solution:
    def equalFrequency(self, word: str) -> bool:
        counts = Counter(word)
        for index in range(len(word)):
            counts[word[index]] -= 1
            if counts[word[index]] == 0:
                del counts[word[index]]
            if len(set(counts.values())) <= 1:
                return True
            counts[word[index]] += 1
        return False
