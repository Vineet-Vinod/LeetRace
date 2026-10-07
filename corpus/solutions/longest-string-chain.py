class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        longest = {}
        for word in sorted(words, key=len):
            best = 1
            for index in range(len(word)):
                predecessor = word[:index] + word[index + 1 :]
                best = max(best, longest.get(predecessor, 0) + 1)
            longest[word] = max(longest.get(word, 0), best)
        return max(longest.values())
