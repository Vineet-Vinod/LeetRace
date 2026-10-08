class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        return sum(count % 2 for count in Counter(s).values()) <= 1
