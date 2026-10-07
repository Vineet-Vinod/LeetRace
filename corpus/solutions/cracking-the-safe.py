class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        a = [0] * (n * k + 1)
        sequence = []

        def visit(t, period):
            if t > n:
                if n % period == 0:
                    sequence.extend(a[1 : period + 1])
                return
            a[t] = a[t - period]
            visit(t + 1, period)
            for digit in range(a[t - period] + 1, k):
                a[t] = digit
                visit(t + 1, t)

        visit(1, 1)
        cycle = "".join(map(str, sequence))
        return (cycle * n)[: len(cycle) + n - 1]
