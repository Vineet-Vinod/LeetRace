class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        chars = list(s)
        for i in range(len(chars) - 1, -1, -1):
            for value in range(ord(chars[i]) + 1, ord("a") + k):
                ch = chr(value)
                if (i and chars[i - 1] == ch) or (i > 1 and chars[i - 2] == ch):
                    continue
                chars[i] = ch
                for j in range(i + 1, len(chars)):
                    for value2 in range(ord("a"), ord("a") + k):
                        ch2 = chr(value2)
                        if ch2 != chars[j - 1] and (j < 2 or ch2 != chars[j - 2]):
                            chars[j] = ch2
                            break
                return "".join(chars)
        return ""
