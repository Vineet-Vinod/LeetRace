class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        permitted = set(allowed)
        return sum(all(char in permitted for char in word) for word in words)
