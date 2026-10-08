class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        previous = [0] * (len(word2) + 1)
        for left in word1:
            current = [0]
            for index, right in enumerate(word2, start=1):
                if left == right:
                    current.append(previous[index - 1] + 1)
                else:
                    current.append(max(previous[index], current[-1]))
            previous = current
        return len(word1) + len(word2) - 2 * previous[-1]
