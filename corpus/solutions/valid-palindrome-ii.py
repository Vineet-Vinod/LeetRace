class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1
        return (
            left >= right or palindrome(left + 1, right) or palindrome(left, right - 1)
        )
