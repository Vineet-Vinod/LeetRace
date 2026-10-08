class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        left = sum(
            amount if direction == 0 else -amount for direction, amount in shift
        ) % len(s)
        return s[left:] + s[:left]
