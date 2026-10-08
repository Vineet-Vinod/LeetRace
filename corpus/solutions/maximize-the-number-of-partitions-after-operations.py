class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        if k == 26:
            return 1
        states = {(0, False): 0}
        for ch in s:
            bit = 1 << (ord(ch) - 97)
            nxt = {}
            for (mask, changed), count in states.items():
                choices = [bit] if changed else [1 << c for c in range(26)]
                for b in choices:
                    used = changed or b != bit
                    newmask = mask | b
                    value = count
                    if newmask.bit_count() > k:
                        newmask = b
                        value += 1
                    key = (newmask, used)
                    if value > nxt.get(key, -1):
                        nxt[key] = value
            states = nxt
        return max(states.values()) + 1
