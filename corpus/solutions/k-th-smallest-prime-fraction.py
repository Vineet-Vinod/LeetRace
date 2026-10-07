from fractions import Fraction


class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        heap = [
            (Fraction(arr[index], arr[-1]), index, len(arr) - 1)
            for index in range(len(arr) - 1)
        ]
        heapify(heap)
        for _ in range(k):
            _, numerator, denominator = heappop(heap)
            if denominator - 1 > numerator:
                next_denominator = denominator - 1
                heappush(
                    heap,
                    (
                        Fraction(arr[numerator], arr[next_denominator]),
                        numerator,
                        next_denominator,
                    ),
                )
        return [arr[numerator], arr[denominator]]
