class Solution:
    def numSub(self, s: str) -> int:
        mod = 10**9 + 7
        run = answer = 0
        for char in s:
            if char == "1":
                run += 1
            else:
                run = 0
            answer = (answer + run) % mod
        return answer
