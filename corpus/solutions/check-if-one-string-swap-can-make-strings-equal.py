class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        differences = [(a, b) for a, b in zip(s1, s2) if a != b]
        return not differences or (
            len(differences) == 2 and differences[0] == differences[1][::-1]
        )
