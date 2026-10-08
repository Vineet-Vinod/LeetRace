class Solution:
    def getSmallestString(self, s: str) -> str:
        chars = list(s)
        for i in range(len(chars) - 1):
            if int(chars[i]) % 2 == int(chars[i + 1]) % 2 and chars[i] > chars[i + 1]:
                chars[i], chars[i + 1] = chars[i + 1], chars[i]
                break
        return "".join(chars)
