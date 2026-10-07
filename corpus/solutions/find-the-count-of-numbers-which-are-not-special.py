class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:  # noqa: E741 - names match the required candidate keyword interface.
        limit = math.isqrt(r)
        sieve = bytearray(b"\x01") * (limit + 1)
        if limit >= 0:
            sieve[0] = 0
        if limit >= 1:
            sieve[1] = 0
        for prime in range(2, math.isqrt(limit) + 1):
            if sieve[prime]:
                start = prime * prime
                sieve[start : limit + 1 : prime] = b"\x00" * (
                    ((limit - start) // prime) + 1
                )
        special = sum(
            1
            for prime in range(2, limit + 1)
            if sieve[prime] and l <= prime * prime <= r
        )
        return r - l + 1 - special
