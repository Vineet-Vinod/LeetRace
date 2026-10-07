class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 10**9 + 7
        answer = 0
        run = 0
        previous = ""
        for ch in s:
            run = run + 1 if ch == previous else 1
            answer += run
            previous = ch
        return answer % mod
