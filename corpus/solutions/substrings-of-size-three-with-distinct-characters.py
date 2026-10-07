class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        return sum(len(set(s[index : index + 3])) == 3 for index in range(len(s) - 2))
