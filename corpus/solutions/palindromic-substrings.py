class Solution:
    def countSubstrings(self, s: str) -> int:
        answer = 0
        for center in range(2 * len(s) - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < len(s) and s[left] == s[right]:
                answer += 1
                left -= 1
                right += 1
        return answer
