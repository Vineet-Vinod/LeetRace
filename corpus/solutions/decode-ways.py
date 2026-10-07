class Solution:
    def numDecodings(self, s: str) -> int:
        two_back = 1
        one_back = int(s[0] != "0")
        for i in range(1, len(s)):
            current = 0
            if s[i] != "0":
                current += one_back
            if 10 <= int(s[i - 1 : i + 1]) <= 26:
                current += two_back
            two_back, one_back = one_back, current
        return one_back
