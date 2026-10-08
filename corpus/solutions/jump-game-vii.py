class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        reachable = [False] * n
        reachable[0] = True
        active = 0
        for i in range(1, n):
            entering = i - minJump
            leaving = i - maxJump - 1
            if entering >= 0 and reachable[entering]:
                active += 1
            if leaving >= 0 and reachable[leaving]:
                active -= 1
            reachable[i] = s[i] == "0" and active > 0
        return reachable[-1]
