class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        first, second = Counter(word1), Counter(word2)
        for char1 in list(first):
            for char2 in list(second):
                first[char1] -= 1
                second[char2] -= 1
                first[char2] += 1
                second[char1] += 1
                distinct1 = sum(count > 0 for count in first.values())
                distinct2 = sum(count > 0 for count in second.values())
                if distinct1 == distinct2:
                    return True
                first[char1] += 1
                second[char2] += 1
                first[char2] -= 1
                second[char1] -= 1
        return False
