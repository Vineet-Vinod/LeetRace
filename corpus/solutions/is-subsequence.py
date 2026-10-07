class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        it = iter(t)
        return all(any(ch == target for ch in it) for target in s)
