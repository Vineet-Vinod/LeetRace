class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {char: index for index, char in enumerate(order)}
        for first, second in zip(words, words[1:]):
            for a, b in zip(first, second):
                if a != b:
                    if rank[a] > rank[b]:
                        return False
                    break
            else:
                if len(first) > len(second):
                    return False
        return True
