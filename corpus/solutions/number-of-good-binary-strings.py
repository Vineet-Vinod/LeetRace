class Solution:
    def goodBinaryStrings(
        self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int
    ) -> int:
        mod = 10**9 + 7
        ways = [0] * (maxLength + 1)
        ways[0] = 1
        for length in range(1, maxLength + 1):
            if length >= oneGroup:
                ways[length] += ways[length - oneGroup]
            if length >= zeroGroup:
                ways[length] += ways[length - zeroGroup]
            ways[length] %= mod
        return sum(ways[minLength:]) % mod
