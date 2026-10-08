class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        low, high = 10 ** (n - 1), 10**n - 1
        for half in range(high, low - 1, -1):
            digits = str(half)
            palindrome = int(digits + digits[::-1])
            minimum_factor = max(low, (palindrome + high - 1) // high)
            # Every even-length decimal palindrome has a factor divisible by 11.
            for factor in range(high - high % 11, minimum_factor - 1, -11):
                if palindrome % factor == 0 and low <= palindrome // factor <= high:
                    return palindrome % 1337
        raise ValueError("No palindrome product")
