class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10**9 + 7
        learned = [0] * (n + 1)
        learned[1] = 1
        sharing = 0
        for day in range(2, n + 1):
            if day - delay >= 1:
                sharing = (sharing + learned[day - delay]) % mod
            if day - forget >= 1:
                sharing = (sharing - learned[day - forget]) % mod
            learned[day] = sharing
        return sum(learned[max(1, n - forget + 1) : n + 1]) % mod
