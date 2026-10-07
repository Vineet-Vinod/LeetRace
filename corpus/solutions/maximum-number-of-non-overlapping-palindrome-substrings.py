class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        answer = 0
        start = 0
        end = k
        while end <= len(s):
            short = s[end - k : end]
            long = s[end - k - 1 : end] if end - k - 1 >= start else ""
            if end - k >= start and short == short[::-1] or long and long == long[::-1]:
                answer += 1
                start = end
                end += k
            else:
                end += 1
        return answer
