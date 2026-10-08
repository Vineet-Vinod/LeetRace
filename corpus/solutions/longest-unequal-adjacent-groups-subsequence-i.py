class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        if not words:
            return []
        result = [words[0]]
        previous = groups[0]
        for word, group in zip(words[1:], groups[1:]):
            if group != previous:
                result.append(word)
                previous = group
        return result
