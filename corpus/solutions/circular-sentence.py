class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        return all(
            words[i][-1] == words[(i + 1) % len(words)][0] for i in range(len(words))
        )
