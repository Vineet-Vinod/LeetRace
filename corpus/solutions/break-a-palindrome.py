class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        chars = list(palindrome)
        for i in range(len(chars) // 2):
            if chars[i] != "a":
                chars[i] = "a"
                return "".join(chars)
        chars[-1] = "b"
        return "".join(chars)
