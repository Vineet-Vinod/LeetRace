class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        shift = k % len(s)
        return s[shift:] + s[:shift]
