class Solution:
    def minimumDistance(self, word: str) -> int:
        def distance(a, b):
            if a == 26 or b == 26:
                return 0
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)

        dp = {26: 0}
        previous = 26
        for character in word:
            current = ord(character) - ord("A")
            next_dp = {}
            for other, cost in dp.items():
                next_dp[other] = min(
                    next_dp.get(other, 10**30), cost + distance(previous, current)
                )
                next_dp[previous] = min(
                    next_dp.get(previous, 10**30), cost + distance(other, current)
                )
            dp = next_dp
            previous = current
        return min(dp.values())
