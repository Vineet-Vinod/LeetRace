class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        signatures = set()
        for word in words:
            signatures.add((tuple(sorted(word[::2])), tuple(sorted(word[1::2]))))
        return len(signatures)
