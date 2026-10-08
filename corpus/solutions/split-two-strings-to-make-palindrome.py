class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def check(first, second):
            left = 0
            right = len(first) - 1
            while left < right and first[left] == second[right]:
                left += 1
                right -= 1

            def palindrome(text, start, end):
                while start < end:
                    if text[start] != text[end]:
                        return False
                    start += 1
                    end -= 1
                return True

            return palindrome(first, left, right) or palindrome(second, left, right)

        return check(a, b) or check(b, a)
