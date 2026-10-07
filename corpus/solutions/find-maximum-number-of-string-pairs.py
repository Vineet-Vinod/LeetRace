class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        seen = set()
        pairs = 0
        for word in words:
            reverse = word[::-1]
            if reverse in seen:
                pairs += 1
            seen.add(word)
        return pairs
