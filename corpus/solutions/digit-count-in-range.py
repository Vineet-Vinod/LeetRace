class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        def count(n: int) -> int:
            ans = 0
            place = 1
            while place <= n:
                upper = n // (place * 10)
                current = n // place % 10
                lower = n % place
                if d:
                    ans += upper * place
                    if current > d:
                        ans += place
                    elif current == d:
                        ans += lower + 1
                elif upper:
                    ans += (upper - 1) * place
                    ans += lower + 1 if current == 0 else place
                place *= 10
            return ans

        return count(high) - count(low - 1)
