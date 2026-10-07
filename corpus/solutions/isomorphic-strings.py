class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(s) == len(t) and len(set(zip(s, t))) == len(set(s)) == len(set(t))
