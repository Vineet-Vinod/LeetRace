class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeats = (len(b) + len(a) - 1) // len(a)
        repeated = a * repeats
        if b in repeated:
            return repeats
        if b in repeated + a:
            return repeats + 1
        return -1
