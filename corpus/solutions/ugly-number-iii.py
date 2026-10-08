class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcm(x: int, y: int) -> int:
            return x // gcd(x, y) * y

        ab, ac, bc = lcm(a, b), lcm(a, c), lcm(b, c)
        abc = lcm(ab, c)

        def count(limit: int) -> int:
            return (
                limit // a
                + limit // b
                + limit // c
                - limit // ab
                - limit // ac
                - limit // bc
                + limit // abc
            )

        low, high = 1, 2 * 10**9
        while low < high:
            middle = (low + high) // 2
            if count(middle) >= n:
                high = middle
            else:
                low = middle + 1
        return low
