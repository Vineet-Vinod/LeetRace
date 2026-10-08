class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        even_positions = (n + 1) // 2
        odd_positions = n // 2

        def modular_power(base, exponent):
            result = 1
            while exponent:
                if exponent % 2:
                    result = result * base % mod
                base = base * base % mod
                exponent //= 2
            return result

        return modular_power(5, even_positions) * modular_power(4, odd_positions) % mod
