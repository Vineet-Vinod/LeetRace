class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts = collections.Counter("".join(words))
        return all(count % len(words) == 0 for count in counts.values())
