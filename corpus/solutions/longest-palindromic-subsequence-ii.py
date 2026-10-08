class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[[0] * n for _ in range(n)] for _ in range(26)]
        best_value = [[0] * n for _ in range(n)]
        best_char = [[-1] * n for _ in range(n)]
        second_value = [[0] * n for _ in range(n)]
        answer = 0
        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                inner_left, inner_right = left + 1, right - 1
                inner_best = best_value[inner_left][inner_right] if length > 2 else 0
                inner_char = best_char[inner_left][inner_right] if length > 2 else -1
                inner_second = (
                    second_value[inner_left][inner_right] if length > 2 else 0
                )
                top_value, top_char, next_value = 0, -1, 0
                left_char = ord(s[left]) - 97
                right_char = ord(s[right]) - 97
                for char in range(26):
                    best = 0
                    if left + 1 <= right:
                        best = max(best, dp[char][left + 1][right])
                    if left <= right - 1:
                        best = max(best, dp[char][left][right - 1])
                    if left_char == char and right_char == char:
                        inside = inner_second if inner_char == char else inner_best
                        best = max(best, inside + 2)
                    dp[char][left][right] = best
                    if best > top_value:
                        next_value = top_value
                        top_value, top_char = best, char
                    elif best > next_value:
                        next_value = best
                    answer = max(answer, best)
                best_value[left][right] = top_value
                best_char[left][right] = top_char
                second_value[left][right] = next_value
        return answer
