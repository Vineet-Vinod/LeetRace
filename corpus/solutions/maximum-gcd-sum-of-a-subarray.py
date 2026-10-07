from math import gcd


class Solution:
    def maxGcdSum(self, nums: list[int], k: int) -> int:
        prefix = [0]
        states = []
        answer = 0
        for i, x in enumerate(nums):
            prefix.append(prefix[-1] + x)
            new = []
            for g, left in states + [(x, i)]:
                g = gcd(g, x)
                if not new or new[-1][0] != g:
                    new.append((g, left))
            states = new
            for g, left in states:
                if i - left + 1 >= k:
                    answer = max(answer, g * (prefix[i + 1] - prefix[left]))
        return answer
