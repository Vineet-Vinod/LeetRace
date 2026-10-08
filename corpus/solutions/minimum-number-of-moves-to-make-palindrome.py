class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        chars = list(s)
        moves = 0
        while chars:
            j = len(chars) - 1
            while chars[j] != chars[0]:
                j -= 1
            if j == 0:
                moves += len(chars) // 2
                chars.pop(0)
            else:
                moves += len(chars) - 1 - j
                chars.pop(j)
                chars.pop(0)
        return moves
