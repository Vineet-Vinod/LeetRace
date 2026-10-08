from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        dictionary = set(words)
        answer = []
        for word in words:
            dp = [-1] * (len(word) + 1)
            dp[0] = 0
            for end in range(1, len(word) + 1):
                for start in range(end):
                    if dp[start] >= 0 and word[start:end] in dictionary:
                        dp[end] = max(dp[end], dp[start] + 1)
            if dp[-1] >= 2:
                answer.append(word)
        return sorted(answer)
