class Solution:
    def makePalindrome(self, s: str) -> bool:
        mismatches = sum(s[left] != s[len(s) - 1 - left] for left in range(len(s) // 2))
        return mismatches <= 2
