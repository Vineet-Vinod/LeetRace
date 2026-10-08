class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i = j = 0
        result = []
        while i < len(word1) and j < len(word2):
            if word1[i:] > word2[j:]:
                result.append(word1[i])
                i += 1
            else:
                result.append(word2[j])
                j += 1
        result.append(word1[i:])
        result.append(word2[j:])
        return "".join(result)
