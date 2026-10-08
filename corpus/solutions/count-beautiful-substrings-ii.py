class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        from collections import Counter

        period = 1
        while period * period % k:
            period += 1
        seen = Counter({(0, 0): 1})
        balance = vowels = answer = 0
        for c in s:
            if c in "aeiou":
                vowels += 1
                balance += 1
            else:
                balance -= 1
            key = (balance, vowels % period)
            answer += seen[key]
            seen[key] += 1
        return answer
