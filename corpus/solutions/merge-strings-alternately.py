class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out = []
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                out.append(word1[i])
            if i < len(word2):
                out.append(word2[i])
        return "".join(out)
