class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        changes = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            amount = 1 if direction else -1
            changes[start] += amount
            changes[end + 1] -= amount
        result: list[str] = []
        shift = 0
        for index, char in enumerate(s):
            shift = (shift + changes[index]) % 26
            result.append(chr((ord(char) - ord("a") + shift) % 26 + ord("a")))
        return "".join(result)
